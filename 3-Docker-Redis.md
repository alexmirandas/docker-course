### Ejercicio: Crear y Dockerizar una Aplicación Web con Flask, PostgreSQL y Redis

Crear una aplicación web con Flask, PostgreSQL y Redis. La aplicación permitirá a los usuarios añadir elementos a una lista y recuperar la lista de elementos.
Utilizaremos Redis para almacenar el caché de la lista de elementos.
Utilizaremos volúmenes locales para persistir los datos de PostgreSQL y Redis.

#### Parte 1: Crear la Aplicación Web

1. **Instala Flask, psycopg2 y redis-py**: Si aún no los tienes, instala Flask, psycopg2 y redis utilizando pip:
   ```bash
   pip install flask psycopg2-binary redis
   ```

2. **Crea la estructura del proyecto**: Crea un directorio para tu proyecto y dentro de él, crea los siguientes archivos:
   ```plaintext
   my_flask_app/
   ├── app.py
   ├── requirements.txt
   ├── init_db.py
   ├── entrypoint.sh
   └── init_db.sh
   ```

3. **Escribe el código de la aplicación**: En `app.py`, escribe el siguiente código para una aplicación Flask que interactúe con PostgreSQL y Redis:
   ```python
   from flask import Flask, request, jsonify
   import psycopg2
   import redis
   import json

   app = Flask(__name__)
   cache = redis.Redis(host='redis', port=6379)

   def get_db_connection():
       conn = psycopg2.connect(host="db", database="mydatabase", user="myuser", password="mypassword")
       return conn

   def get_cache():
       entries = cache.get('entries')
       if entries:
           return json.loads(entries)
       else:
           return None

   def set_cache(entries):
       cache.set('entries', json.dumps(entries))

   @app.route('/')
   def home():
       return "¡Hola, Docker con PostgreSQL y Redis!"

   @app.route('/add', methods=['POST'])
   def add_entry():
       data = request.get_json()
       name = data['name']
       conn = get_db_connection()
       cur = conn.cursor()
       cur.execute('INSERT INTO entries (name) VALUES (%s)', (name,))
       conn.commit()
       cur.close()
       conn.close()

       entries = get_entries_from_db()
       set_cache(entries)

       return jsonify({"message": "Entry added"}), 201

   def get_entries_from_db():
       conn = get_db_connection()
       cur = conn.cursor()
       cur.execute('SELECT * FROM entries')
       entries = cur.fetchall()
       cur.close()
       conn.close()
       return entries

   @app.route('/entries', methods=['GET'])
   def get_entries():
       entries = get_cache()
       if entries is None:
           entries = get_entries_from_db()
           set_cache(entries)
       return jsonify(entries)

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

4. **Especifica las dependencias**: En el archivo `requirements.txt`, añade Flask, psycopg2 y redis:
   ```plaintext
   Flask==2.1.1
   psycopg2-binary==2.9.3
   redis==4.2.0
   ```

5. **Inicializa la base de datos**: En `init_db.py`, escribe el siguiente código para crear la tabla en PostgreSQL:
   ```python
   import psycopg2

   conn = psycopg2.connect(host="db", database="mydatabase", user="myuser", password="mypassword")
   cur = conn.cursor()

   cur.execute('''
       CREATE TABLE IF NOT EXISTS entries (
           id SERIAL PRIMARY KEY,
           name TEXT NOT NULL
       )
   ''')

   conn.commit()
   cur.close()
   conn.close()
   ```

6. **Crea el script de inicialización de la base de datos**: En `init_db.sh`, escribe el siguiente código:
   ```bash
   #!/bin/bash
   # Espera hasta que PostgreSQL esté listo
   while ! pg_isready -h db -p 5432 -U myuser > /dev/null 2> /dev/null; do
       sleep 1
   done

   python init_db.py
   ```

7. **Crea el punto de entrada del contenedor**: En `entrypoint.sh`, escribe el siguiente código:
   ```bash
   #!/bin/bash

   set -e

   # Ejecuta el script de inicialización de la base de datos
   /app/init_db.sh

   # Ejecuta el servidor Flask
   exec "$@"
   ```

   Haz que los scripts sean ejecutables:
   ```bash
   chmod +x entrypoint.sh init_db.sh
   ```

#### Parte 2: Dockerizar la Aplicación y los Servicios

1. **Crea un Dockerfile**: En el directorio `my_flask_app`, crea un archivo llamado `Dockerfile` y añade el siguiente contenido:
   ```Dockerfile
   # Utiliza una imagen base de Python
   FROM python:3.9-slim

   # Establece el directorio de trabajo
   WORKDIR /app

   # Copia los archivos de la aplicación al contenedor
   COPY . /app

   # Instala las dependencias
   RUN pip install -r requirements.txt

   # Copia los scripts de inicialización y los hace ejecutables
   COPY entrypoint.sh /entrypoint.sh
   RUN chmod +x /entrypoint.sh
   COPY init_db.sh /init_db.sh
   RUN chmod +x /init_db.sh

   # Expone el puerto que la aplicación usará
   EXPOSE 5000

   # Define el punto de entrada y el comando para ejecutar la aplicación
   ENTRYPOINT ["/entrypoint.sh"]
   CMD ["python", "app.py"]
   ```

2. **Crea un archivo `docker-compose.yml`**: En el directorio `my_flask_app`, crea un archivo llamado `docker-compose.yml` con el siguiente contenido:
   ```yaml
   version: '3.8'
   services:
     web:
       build: .
       ports:
         - "5000:5000"
       volumes:
         - .:/app
       depends_on:
         - db
         - redis
     db:
       image: postgres:13
       environment:
         POSTGRES_DB: mydatabase
         POSTGRES_USER: myuser
         POSTGRES_PASSWORD: mypassword
       volumes:
         - pgdata:/var/lib/postgresql/data
     redis:
       image: "redis:6.0"
       volumes:
         - redisdata:/data
   volumes:
     pgdata:
     redisdata:
   ```

3. **Construye y ejecuta los contenedores**:
   ```bash
   docker-compose up --build
   ```

4. **Accede a la aplicación**: Abre tu navegador y visita `http://localhost:5000`. Deberías ver el mensaje "¡Hola, Docker con PostgreSQL y Redis!".

5. **Prueba la aplicación**:
   - Para agregar una entrada, puedes usar `curl` o Postman:
     ```bash
     curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"name": "Prueba"}'
     ```
   - Para ver las entradas:
     ```bash
     curl http://localhost:5000/entries
     ```
