FROM python:3.10

RUN apt-get update
RUN apt-get upgrade
RUN apt-get -y install netcat
RUN apt-get clean

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY  requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

RUN chmod +x ./run.sh

RUN chmod -R 777 ./