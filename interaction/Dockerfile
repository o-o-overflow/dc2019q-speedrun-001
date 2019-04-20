FROM python:2.7-alpine

ENV TERM linux

RUN echo "travis_fold:start:DIapt\033[33;1minteractions Dockerfile pkgs\033[0m" && \
    apk update && apk add --no-cache git netcat-openbsd openssl-dev libffi-dev g++ linux-headers make bash && \
    echo "\ntravis_fold:end:DIapt\r"

COPY payload /payload
COPY exploit.sh /exploit.sh

COPY check.sh /check.sh


