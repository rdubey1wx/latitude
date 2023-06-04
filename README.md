# Data Engineering Coding Challenge
Hi, thank you for your time in solving the coding challenge. The goal is to see how your approach to problem-solving, and how you structure your code and hand it over to the team for review.

You can solve any one of the following problem statements. This README describes evaluation criteria, problem statements, and also some of the choices which you might have to make. If you need any further information, please reach out we are happy to help.

## Evaluation Criteria
- Code structure, and README instructions to review and run code
- Basic engineering principles
- Testing strategies

## Problem Statement - 1 (Anonymize customer information)
Imagine you are working on a project where you have to process customer data and generate insights. Considering this data has customer information and to generate insights, multiple teams will be using this data. To ensure we handle customer information with care, and not make it visible to everyone on the team one requirement is to anonymize customer information before it's loaded into the warehouse for insights generation.

- You will get this data in CSV files which will have customer personal information like first_name, last_name, address, date_of_birth
- Write code to generate a CSV file containing first_name, last_name, address, date_of_birth
- Load generated CSV in the previous step, anonymize data, and output anonymized data to a different file
- Columns to anonymise are first_name, last_name and address

## Choices
- You can use any language or any platform
- You can use any package or library unless specified in coding challenge
- Bonus points if you bundle your code using Docker(Dockerfile) that can be used to run the code
- You can share code either using Github, bitbucket, or zip in the email
- We are not expecting to enter data on command prompt, you can use any faker library to generate mock data
- Include a README file describing how we can run and test

## Setup guide
- Copy the git repo in your local machine or in any Elastic instance with Docker.(Below steps follow linux directory pattern. For Windows or any other os please refer the respective commands.)
- It will create following directory structure in your machine.Please ensure your local directory structure is adhering to the below pattern.
   lvl0--->latitude
            lvl1----> anonymize
                    lvl2-------> anonymize.py
                    lvl2-------> config.yaml
                    lvk2-------> Dockerfile
                    lvl2-------> requirements.txt
- Switch to anonymize directory by typing following command  cd latitude/anonymize
- Type Docker --version and check the reponse. (Note :: This code waas tested on Docker version 20.10.15)
- If the above command does not render the Docker version or you see any other output. Most likely Docker is not installed in your machine. Please download and install Docker.
- Run the below command to build the Docker image from the anonymize directory.
    Docker build .
- It will take few seconds to build the image. Wait till the command prompt is ready.
- Next run Docker images.
- Copy the IMAGE ID rendered from the above command. Say the IMAGE ID is 33fe87f6722b.
- Run docker run <IMAGE ID>. In our case it should be docker run 33fe87f6722b.
- Check the logs rendered. If there are no errors that means the Python script has run successfully.
- Next a Docker nteractive terminal to verify the files.
- Run docker run -it 33fe87f6722b /bin/bash
- Terminal will open /anonymize directory
- Run the Python script directly from here by typing Python anonymize.py command.
- The csv file will be created in the /anonymize/output directory and the anonymized file will be creaed the /anonymize/hashed folder.
- Check the logs in the terminal to identify the correct file name as the file name gets suffixed with unique UUID.
- User can change the YAML files i.e. /anonymize/config.yaml and try re-running the pythin script.