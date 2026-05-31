FROM python:3.9-alpine3.16

WORKDIR /app

COPY Python/ /app/

RUN apk add --no-cache curl=7.83.1-r4 || apk add --no-cache curl

ENV PYTHONUNBUFFERED=1

CMD ["python", "calculator.py"]
