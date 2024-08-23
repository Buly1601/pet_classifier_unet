FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip

WORKDIR /servicio_social
COPY . . 
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
