from faker import Faker
import pandas as pd
import os,uuid,logging
import hashlib
import yaml

logging.basicConfig(
    format="%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO
)

UUID=str(uuid.uuid4())

class Customer():
    """
    Customer Class to specify setter method for generating Customer attributes and methods to anonymkze any given attributes.

    Args: 
        record_count (Int) : Number of sample records that user would like to genrate. Users need to append this info in Config.yaml file.

    """
    def __init__(self,record_count) -> None:
        self.record_count=record_count
        self.faker=Faker()
        self.df=pd.DataFrame()

    @property
    def first_name(self):
        return self.faker.first_name()
    
    @property
    def last_name(self):
        return self.faker.last_name()

    @property
    def address(self):
        return self.faker.address().replace('\n',',')

    @property
    def date_of_birth(self):
        return self.faker.date_of_birth(minimum_age=18, maximum_age=99).strftime('%Y-%m-%d')

    def anonymize_series(self,series):
        return series.apply(lambda x:hashlib.sha256(x.encode()).hexdigest())
       
    def create_customer_datasets(self, custom_method):
        data=[getattr(self, custom_method) for _ in range(self.record_count)]
        self.df[custom_method]=data
        return self.df


def create_os_path(Path):
    """
    Creates directories structure to ensure output files are kept in their designated directories.

    Args:
        Path (str) : Path where the User would like to  generate the files.
    Currently the csv file would be generated under anonymize/output/ directory & the anonymised filed would be generated under anonymize/hashed/ directory

    """
    isExist = os.path.exists(os.getcwd() + Path)
    if not isExist:
        os.makedirs(os.getcwd() + Path)
        logging.info(f"The new directory path {Path} is created!")
    else:
        logging.info(f"Given path {Path} exists aleady. No action needed.")
    return (os.getcwd() + Path)


def create_customer_datasets(customer_obj,customer_attributes):
    """
    Generates sample CSV file for Customer. 

    Args:
        customer_obj <obj>: Object for customer class.
        customer_attributes: Attributes that needs to be included the csv file. It is read from the config.yaml file.

    """
    try:
        CustomerDF = [customer_obj.create_customer_datasets(x) for x in customer_attributes][0]
        Path = create_os_path("/output/")
        FileName = Path + "customer_details_" + UUID + ".csv"
        CustomerDF.to_csv(FileName,index=False)
        logging.info("Customer csv file created successfully.")
        logging.info(f"CSV File Name :=>{FileName}")
    except Exception as e:
        logging.error(e)
        exit()
    return FileName


def anonymize_customer_data(customer_obj,anonymize_column_list,csv_FileName):
    """
    Anonymizes the given customer attributes.

    Args:
        customer_obj <obj>: Object for customer class.
        anonymize_column_list: Attributes that needs to be anonymised in the csv file. It is read from the config.yaml file.
        csv_FileName: File name with path that needs to be anonymised.
    """
    CustomerDF = pd.read_csv(csv_FileName)
    try:
        for attr in anonymize_column_list:
            CustomerDF[attr] = customer_obj.anonymize_series(CustomerDF[attr])
        Path = create_os_path("/hashed/")
        FileName = Path +  "customer_details_anonymised_" + UUID + ".csv"
        CustomerDF.to_csv(FileName,index=False)
        logging.info("Customer File anonymized successfully.")
        logging.info(f"Anonymized File Name :=>{FileName}")
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    YmlPath=os.getcwd() + "/config.yaml"
    try:
        with open(YmlPath) as f:
            yml_dict = yaml.safe_load(f)
            config_dict = yml_dict.get("anonymize_params")
            customer_attributes = config_dict.get('customer_attributes_list')
            anonymize_column_list = config_dict.get('anonymize_column_list')
            record_count = config_dict.get('record_count')
            logging.info("customer_attributes,anonymize_column_list & record_count retrieved from yaml :=> {0},{1} & {2} respectively."
                         .format(customer_attributes,anonymize_column_list,record_count))
    except Exception as e:
        logging.error(f'Exception raised while accessing Yaml Config: {e}.Exiting.....')
        exit()
    
    new_customer_csv = Customer(record_count)
    FileName = create_customer_datasets(new_customer_csv,customer_attributes)
    anonymize_customer_data(new_customer_csv,anonymize_column_list,FileName)
    logging.info("Process completed successfully.Cheers!!!")
