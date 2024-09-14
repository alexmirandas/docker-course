Construir y desplegar una aplicación web en Python con Flask como framework web y SQLAlchemy para interactuar con PostgreSQL.

### 1. Preparar la Aplicación en Python

Primero, crea una aplicación en Python que se conecte a PostgreSQL y permita almacenar y consultar registros de una lista de tareas.

#### 1.1. Crear el archivo `app.py`

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        return jsonify([{'id': task.id, 'name': task.name, 'done': task.done} for task in tasks])
    elif request.method == 'POST':
        data = request.get_json()
        new_task = Task(name=data['name'], done=data['done'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'id': new_task.id, 'name': new_task.name, 'done': new_task.done})

@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'GET':
        return jsonify({'id': task.id, 'name': task.name, 'done': task.done})
    elif request.method == 'PUT':
        data = request.get_json()
        task.name = data['name']
        task.done = data['done']
        db.session.commit()
        return jsonify({'id': task.id, 'name': task.name, 'done': task.done})
    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

#### 1.2. Crear el archivo `Dockerfile`

```Dockerfile
FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
```

#### 1.3. Crear el archivo `requirements.txt`

```text
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
psycopg2-binary==2.9.1
```

### 2. Inicializar el Proyecto

#### 2.1. Crear el archivo `init.sql`

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);
```

#### 2.2. Crear el archivo `docker-compose.yml`

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: tasks_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

  web:
    build: .
    ports:
      - "8080:8080"
    environment:
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: user
      DB_PASSWORD: password
      DB_NAME: tasks_db
    depends_on:
      - db

volumes:
  postgres_data:
```

### 3. Construir y Desplegar la Aplicación

#### 3.1. Ejecutar Docker Compose

```sh
docker-compose up --build -d
```

### 4. Probar la Aplicación

#### 4.1. Agregar un registro usando POST:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"name": "Tarea de ejemplo", "done": false}' http://localhost:8080/tasks
```

#### 4.2. Petición GET para obtener todas las tareas:

```sh
curl http://localhost:8080/tasks
```
