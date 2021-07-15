FROM python:3.9
WORKDIR /home/microservice/calculator
COPY Calculator /home/microservice/calculator
RUN pip install -r requirements.txt