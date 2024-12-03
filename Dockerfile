FROM python:3.10-slim

WORKDIR /api

COPY ./django/system/requirements/main.txt .

COPY ./django .

RUN pip install --no-cache-dir -r main.txt

EXPOSE 8000

CMD [ "bash", "django/docker/build.sh" ]
