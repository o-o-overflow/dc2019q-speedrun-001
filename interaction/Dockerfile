FROM python:2.7-alpine

ENV TERM linux

RUN apk update && apk add --no-cache git netcat-openbsd openssl-dev libffi-dev g++ linux-headers make bash

COPY payload /payload
COPY exploit.sh /exploit.sh

COPY check.sh /check.sh


