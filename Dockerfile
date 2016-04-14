FROM python:2.7.11-slim

ADD . /srv
RUN pip install -r /srv/requirements.txt

EXPOSE 8000
ENV HOME /srv
WORKDIR /hsrv