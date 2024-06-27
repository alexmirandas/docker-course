FROM golang:1.18-alpine

WORKDIR /app

# Instalar el cliente de PostgreSQL
RUN apk add --no-cache postgresql-client

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY *.go ./
COPY wait-for-it.sh ./
RUN chmod +x wait-for-it.sh

RUN go build -o /docker-golang-app

EXPOSE 8080

CMD [ "/app/wait-for-it.sh", "db:5432", "--", "/docker-golang-app" ]
