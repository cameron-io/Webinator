FROM python:alpine
WORKDIR /var/lib/webinator
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD . .
CMD python3 -m flask --app src/app run
