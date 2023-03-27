FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive


COPY flag.txt /tmp/flag.txt

COPY run.py /tmp/run.py

RUN apt update

RUN apt install python3 -y

CMD [ "python3", "/tmp/run.py" ]
