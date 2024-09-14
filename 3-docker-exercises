### **Ejercicio 1: Descargar y ejecutar una imagen básica**
1. **Objetivo**: Descargar y ejecutar un contenedor desde Docker Hub.
2. **Comandos a usar**: `docker pull`, `docker run`, `docker ps`.
   
   **Instrucciones**:
   - Descarga la imagen de **alpine** (un contenedor ligero de Linux) con el comando:
     ```bash
     docker pull alpine
     ```
   - Ejecuta el contenedor con el comando:
     ```bash
     docker run -it alpine /bin/sh
     ```
   - Verifica que el contenedor se está ejecutando con:
     ```bash
     docker ps
     ```

---

### **Ejercicio 2: Crear y gestionar contenedores**
1. **Objetivo**: Crear, detener, iniciar y eliminar contenedores.
2. **Comandos a usar**: `docker run`, `docker stop`, `docker start`, `docker rm`, `docker ps -a`.

   **Instrucciones**:
   - Crea un contenedor con la imagen de **nginx**:
     ```bash
     docker run -d --name webserver nginx
     ```
   - Detén el contenedor:
     ```bash
     docker stop webserver
     ```
   - Inicia el contenedor nuevamente:
     ```bash
     docker start webserver
     ```
   - Elimina el contenedor:
     ```bash
     docker rm webserver
     ```

---

### **Ejercicio 3: Listar, eliminar y limpiar imágenes**
1. **Objetivo**: Gestionar las imágenes locales de Docker.
2. **Comandos a usar**: `docker images`, `docker rmi`.

   **Instrucciones**:
   - Lista las imágenes descargadas localmente:
     ```bash
     docker images
     ```
   - Elimina una imagen de tu sistema usando su ID:
     ```bash
     docker rmi [id_imagen]
     ```

---

### **Ejercicio 4: Crear y usar un Dockerfile**
1. **Objetivo**: Crear tu propia imagen personalizada a partir de un Dockerfile.
2. **Comandos a usar**: `docker build`, `docker run`.

   **Instrucciones**:
   - Crea un archivo `Dockerfile` con el siguiente contenido:
     ```dockerfile
     FROM ubuntu
     RUN apt-get update && apt-get install -y curl
     CMD ["curl", "--version"]
     ```
   - Construye la imagen desde el Dockerfile:
     ```bash
     docker build -t custom_ubuntu .
     ```
   - Ejecuta un contenedor desde la nueva imagen creada:
     ```bash
     docker run custom_ubuntu
     ```

---

### **Ejercicio 5: Almacenamiento persistente con volúmenes**
1. **Objetivo**: Crear un volumen y usarlo en un contenedor.
2. **Comandos a usar**: `docker volume create`, `docker run`, `docker volume ls`.

   **Instrucciones**:
   - Crea un volumen:
     ```bash
     docker volume create mi_volumen
     ```
   - Ejecuta un contenedor de **nginx** usando el volumen para almacenar datos:
     ```bash
     docker run -d --name webserver_vol -v mi_volumen:/usr/share/nginx/html nginx
     ```
   - Verifica los volúmenes disponibles:
     ```bash
     docker volume ls
     ```

---

### **Ejercicio 6: Redes en Docker**
1. **Objetivo**: Crear una red personalizada y conectar contenedores a ella.
2. **Comandos a usar**: `docker network create`, `docker network connect`, `docker network ls`.

   **Instrucciones**:
   - Crea una red llamada `mi_red`:
     ```bash
     docker network create mi_red
     ```
   - Ejecuta un contenedor de **nginx** conectado a esta red:
     ```bash
     docker run -d --name webserver_net --network mi_red nginx
     ```
   - Verifica que el contenedor esté conectado a la red:
     ```bash
     docker network ls
     ```

---

### **Ejercicio 7: Logs y ejecución de comandos en contenedores**
1. **Objetivo**: Consultar logs y ejecutar comandos dentro de contenedores en ejecución.
2. **Comandos a usar**: `docker logs`, `docker exec`.

   **Instrucciones**:
   - Ejecuta un contenedor de **nginx** y observa sus logs:
     ```bash
     docker run -d --name webserver nginx
     docker logs webserver
     ```
   - Ejecuta un comando dentro del contenedor en ejecución (acceder al shell de bash):
     ```bash
     docker exec -it webserver /bin/bash
     ```

---

### **Ejercicio 8: Docker Compose - Configuración multi-servicio**
1. **Objetivo**: Configurar y ejecutar múltiples contenedores con Docker Compose.
2. **Comandos a usar**: `docker-compose up`, `docker-compose down`.

   **Instrucciones**:
   - Crea un archivo `docker-compose.yml` con el siguiente contenido:
     ```yaml
     version: '3.8'
     services:
       web:
         image: nginx
         ports:
           - "8080:80"
       db:
         image: postgres
         environment:
           POSTGRES_USER: admin
           POSTGRES_PASSWORD: password
     ```
   - Levanta los servicios con Docker Compose:
     ```bash
     docker-compose up
     ```
   - Detén los servicios y elimina los contenedores y redes:
     ```bash
     docker-compose down
     ```

---

### **Ejercicio 9: Guardar y cargar imágenes**
1. **Objetivo**: Exportar e importar imágenes de Docker.
2. **Comandos a usar**: `docker save`, `docker load`.

   **Instrucciones**:
   - Guarda una imagen en un archivo tar:
     ```bash
     docker save -o nginx_backup.tar nginx
     ```
   - Carga una imagen desde un archivo tar:
     ```bash
     docker load -i nginx_backup.tar
     ```

---

### **Ejercicio 10: Subir imágenes personalizadas a Docker Hub**
1. **Objetivo**: Crear y subir una imagen a Docker Hub.
2. **Comandos a usar**: `docker tag`, `docker push`.

   **Instrucciones**:
   - Inicia sesión en Docker Hub:
     ```bash
     docker login
     ```
   - Crea una imagen personalizada (usa un Dockerfile de algún ejercicio anterior) y etiqueta la imagen:
     ```bash
     docker tag custom_ubuntu tu_usuario_dockerhub/custom_ubuntu:v1
     ```
   - Sube la imagen a Docker Hub:
     ```bash
     docker push tu_usuario_dockerhub/custom_ubuntu:v1
     ```

