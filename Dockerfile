# Pull base image.
FROM python:3.6

RUN \
  apt-get -y update && \
  apt-get -y install vim

# Install pip packages we need
RUN \
  pip install uwsgi && \
  pip install falcon

ADD . /var/xe-hive-worker

WORKDIR /var/xe-hive-worker

EXPOSE 80

# Run nginx and uwsgi when container starts
ENTRYPOINT uwsgi --ini /var/xe-hive-worker/uwsgi.ini