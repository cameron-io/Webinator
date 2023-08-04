FROM python:alpine
WORKDIR /var/lib/webinator
ADD requirements.txt .
RUN apk update && \
    apk upgrade
RUN pip3 install -r requirements.txt
ADD . .
RUN source .env
CMD python3 -m flask run
