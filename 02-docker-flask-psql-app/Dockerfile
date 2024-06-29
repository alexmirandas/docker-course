FROM python:3.9-alpine

# Instala las dependencias del sistema necesarias para psycopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
