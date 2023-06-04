FROM python:3.9-slim

WORKDIR /anonymize

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . ./

CMD ["python","anonymize.py"]