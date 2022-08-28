FROM python:3.9.12-alpine3.15

ENV TZ=America/Bogota
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app

RUN apk update --no-cache && apk upgrade --no-cache 

RUN apk add --no-cache --virtual .build-deps \
    gcc musl-dev linux-headers bash tzdata  curl

COPY . .

RUN addgroup admin && adduser -S flask -G admin \
    && chown -R flask:admin /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


USER flask
EXPOSE 5000
CMD ["flask", "run"]

HEALTHCHECK --interval=20m --timeout=4s --start-period=30s --retries=5 \
CMD curl -f http://localhost:5000 || exit 1