FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
