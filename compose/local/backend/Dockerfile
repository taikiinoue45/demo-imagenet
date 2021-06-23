FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./compose/local/backend/requirements /root/requirements
COPY ./compose/local/backend/entrypoint.sh /root/entrypoint.sh
RUN pip install --upgrade pip
RUN pip install -r /root/requirements/base.txt
ENTRYPOINT /root/entrypoint.sh
