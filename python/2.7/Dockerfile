FROM ubuntu:14.04

MAINTAINER Thiago Falcao "thiagofalcao@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python2.7 \
    python2.7-dev \
    ssh \
    && apt-get autoremove \
    && apt-get clean

RUN pip install setuptools
RUN pip install virtualenv
RUN pip install nose
RUN pip install mock
RUN pip install coverage
RUN pip install pylint