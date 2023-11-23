FROM python:3.9

#workdir-i ognutyamb chenq grum full path to manage.py
WORKDIR /django_app
COPY . .
EXPOSE 8000
RUN apt-get update && apt-get install -y default-libmysqlclient-dev
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

