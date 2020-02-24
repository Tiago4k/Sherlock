FROM python:3.7-slim-stretch

RUN apt update && apt install --no-install-recommends -y python3-dev gcc build-essential

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

RUN pip install -r requirements.txt

RUN chmod +x boot.sh

ENTRYPOINT ["./boot.sh"]