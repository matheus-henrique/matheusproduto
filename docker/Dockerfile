FROM ubuntu:latest
USER root
MAINTAINER Matheus Henrique

RUN apt-get update 
RUN apt-get -y install python3.6
RUN apt-get -y install python3-pip nginx supervisor git git-core libpq-dev python-dev python-virtualenv
RUN rm /etc/nginx/sites-enabled/default

RUN mkdir -p /home/matheus/logs
WORKDIR /home/matheus
RUN git clone https://github.com/matheus-henrique/matheusproduto
WORKDIR /
COPY meusite /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/meusite /etc/nginx/sites-enabled/meusite

COPY gunicorn_conf /home/matheus/matheusproduto/
WORKDIR /home/matheus/matheusproduto/
RUN pip3 install -r requirements.txt

COPY gunicorn.conf /etc/supervisor/conf.d/

RUN supervisord
CMD service nginx restart & gunicorn matheusprodutos.wsgi:application -c /home/matheus/matheusproduto/gunicorn_conf


