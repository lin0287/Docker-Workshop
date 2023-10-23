FROM alpine:3.17.5

WORKDIR /app

RUN apk add python3 py3-pip

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV ENV_1="test"

COPY app/* /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run"]
