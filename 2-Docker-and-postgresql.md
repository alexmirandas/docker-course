### Ejercicio: Crear y Dockerizar una Aplicación Web con Flask y PostgreSQL

#### Parte 1: Crear la Aplicación Web

1. **Instala Flask y psycopg2**: Si aún no los tienes, instala Flask y psycopg2 utilizando pip:
   ```bash
   pip install flask psycopg2-binary
   ```

2. **Crea la estructura del proyecto**: Crea un directorio para tu proyecto y dentro de él, crea un archivo Python llamado `app.py` y un archivo para manejar las dependencias `requirements.txt`:
   ```plaintext
   my_flask_app/
   ├── app.py
   ├── requirements.txt
   └── init_db.py
   ```

3. **Escribe el código de la aplicación**: En `app.py`, escribe el siguiente código para una aplicación Flask simple que interactúe con PostgreSQL:
   ```python
   from flask import Flask, request, jsonify
   import psycopg2

   app = Flask(__name__)

   def get_db_connection():
       conn = psycopg2.connect(host="db", database="mydatabase", user="myuser", password="mypassword")
       return conn

   @app.route('/')
   def home():
       return "¡Hola, Docker con PostgreSQL!"

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
       return jsonify({"message": "Entry added"}), 201

   @app.route('/entries', methods=['GET'])
   def get_entries():
       conn = get_db_connection()
       cur = conn.cursor()
       cur.execute('SELECT * FROM entries')
       entries = cur.fetchall()
       cur.close()
       conn.close()
       return jsonify(entries)

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

4. **Especifica las dependencias**: En el archivo `requirements.txt`, añade Flask y psycopg2:
   ```plaintext
   Flask==2.1.1
   psycopg2-binary==2.9.3
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

#### Parte 2: Dockerizar la Aplicación y la Base de Datos

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

   # Expone el puerto que la aplicación usará
   EXPOSE 5000

   # Define el comando para ejecutar la aplicación
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
     db:
       image: postgres:13
       environment:
         POSTGRES_DB: mydatabase
         POSTGRES_USER: myuser
         POSTGRES_PASSWORD: mypassword
       volumes:
         - pgdata:/var/lib/postgresql/data
   volumes:
     pgdata:
   ```

3. **Inicializa la base de datos**: Crea un archivo `init_db.sh` para inicializar la base de datos y ejecutarlo como un servicio:
   ```bash
   #!/bin/bash
   # Espera hasta que PostgreSQL esté listo
   while ! pg_isready -h db -p 5432 -U myuser > /dev/null 2> /dev/null; do
       sleep 1
   done

   python init_db.py
   ```

4. **Crea un archivo `entrypoint.sh`**: Crea un archivo `entrypoint.sh` para inicializar la base de datos:
   ```bash
   #!/bin/bash

   set -e

   # Ejecuta el script de inicialización de la base de datos
   /app/init_db.sh

   # Ejecuta el servidor Flask
   exec "$@"
   ```

   Modifica el `Dockerfile` para utilizar este script:
   ```Dockerfile
   # Utiliza una imagen base de Python
   FROM python:3.9-slim

   # Establece el directorio de trabajo
   WORKDIR /app

   # Copia los archivos de la aplicación al contenedor
   COPY . /app

   # Instala las dependencias
   RUN pip install -r requirements.txt

   # Copia el script de inicialización y lo hace ejecutable
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

5. **Construye y ejecuta los contenedores**:
   ```bash
   docker-compose up --build
   ```

6. **Accede a la aplicación**: Abre tu navegador y visita `http://localhost:5000`. Deberías ver el mensaje "¡Hola, Docker con PostgreSQL!".

7. **Prueba la aplicación**:
   - Para agregar una entrada, puedes usar `curl` o Postman:
     ```bash
     curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"name": "Prueba"}'
     ```
   - Para ver las entradas:
     ```bash
     curl http://localhost:5000/entries
     ```
