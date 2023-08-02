FROM python3:alpine
WORKDIR /var/lib/webinator
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD . .
CMD make run
