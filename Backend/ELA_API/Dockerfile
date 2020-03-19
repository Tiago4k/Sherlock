FROM python:3.7-slim 

ENV APP_HOME /app

COPY requirements.txt /app/requirements.txt

WORKDIR $APP_HOME

RUN pip install -r requirements.txt
COPY . ./

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app