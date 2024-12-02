FROM python:3.10-slim

WORKDIR /api

COPY ./system/system/requirements/main.txt .

COPY ./system .

RUN pip install --no-cache-dir -r main.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver","0.0.0.0:8000" ]
