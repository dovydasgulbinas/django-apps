FROM python:3.7.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV USE_DEV "true"
ENV USE_GUNICORN "false"

RUN apk update \
    && apk add --no-cache \
        postgresql-client gcc linux-headers libc-dev

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

EXPOSE 8000