# target dev
FROM alpine:latest AS dev
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
# add postgres development libs, python, pip
RUN apk add --no-cache python3 py3-pip postgresql-dev gcc python3-dev musl-dev && \
    pip3 install -r requirements.txt

COPY . /opt/app
RUN sed -i 's/localhost/postgres/1' .pgpass .pg_service.conf
CMD ["bash", "-c", "'python3 ./manage.py migrate && python3 ./manage.py collectstatic --no-input && python3 ./manage.py runserver'"]
