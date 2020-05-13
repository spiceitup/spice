FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app
RUN pip install -r requirements.txt

COPY . /opt/app

EXPOSE 8000
