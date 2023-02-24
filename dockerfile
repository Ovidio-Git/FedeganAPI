FROM python:3.9-slim-buster

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN apt-get update
RUN apt-get install -y libpq-dev gcc
RUN pip install psycopg2-binary
RUN pip install psycopg2
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 3000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]