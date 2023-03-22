FROM python:3-alpine

Run app add --no-cache-openssl

WORKDIR /.

ADD server1.py 

VOLUME /servervol 

VOLUME /clientvol 

CMD ["python","server1.py"]


