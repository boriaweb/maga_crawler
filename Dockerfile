FROM python:3.6
ADD . /maga_crawler
WORKDIR /maga_crawler
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py