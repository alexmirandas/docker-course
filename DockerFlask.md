### Ejercicio: Crear y Dockerizar una Aplicación Web con Flask

#### Parte 1: Crear la Aplicación Web

1. **Instala Flask**: Si aún no lo tienes, instala Flask utilizando pip:
   ```bash
   pip install flask
   ```

2. **Crea la estructura del proyecto**: Crea un directorio para tu proyecto y dentro de él, crea un archivo Python llamado `app.py`:
   ```plaintext
   my_flask_app/
   ├── app.py
   └── requirements.txt
   ```

3. **Escribe el código de la aplicación**: En `app.py`, escribe el siguiente código para una aplicación Flask simple:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "¡Hola, Docker!"

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

4. **Especifica las dependencias**: En el archivo `requirements.txt`, añade Flask:
   ```plaintext
   Flask==2.1.1
   ```

#### Parte 2: Dockerizar la Aplicación

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

2. **Construye la imagen Docker**: En la línea de comandos, navega al directorio `my_flask_app` y ejecuta:
   ```bash
   docker build -t my_flask_app .
   ```

3. **Ejecuta el contenedor Docker**: Después de construir la imagen, ejecuta el contenedor:
   ```bash
   docker run -d -p 5000:5000 my_flask_app
   ```

4. **Accede a la aplicación**: Abre tu navegador y visita `http://localhost:5000`. Deberías ver el mensaje "¡Hola, Docker!".

### Opcional: Docker Compose

Para hacer el ejercicio un poco más avanzado, puedes usar Docker Compose para gestionar tu aplicación.

1. **Crea un archivo `docker-compose.yml`**: En el directorio `my_flask_app`, crea un archivo llamado `docker-compose.yml` con el siguiente contenido:
   ```yaml
   version: '3'
   services:
     web:
       build: .
       ports:
         - "5000:5000"
   ```

2. **Ejecuta la aplicación con Docker Compose**:
   ```bash
   docker-compose up -d
   ```

3. **Accede a la aplicación**: De nuevo, abre tu navegador y visita `http://localhost:5000`.

Este ejercicio te da una buena introducción a la creación de una aplicación web simple con Flask y cómo dockerizarla, así como una pequeña introducción a Docker Compose.