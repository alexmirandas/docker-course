
### 1. **docker --version**
   - **Descripción**: Muestra la versión instalada de Docker.

### 2. **docker pull [nombre_imagen]**
   - **Descripción**: Descarga una imagen desde Docker Hub (o un registro) a tu sistema local.

### 3. **docker images**
   - **Descripción**: Muestra una lista de todas las imágenes almacenadas localmente en tu sistema.

### 4. **docker rmi [id_imagen]**
   - **Descripción**: Elimina una imagen de Docker de tu sistema local.

### 5. **docker run [nombre_imagen]**
   - **Descripción**: Crea y ejecuta un nuevo contenedor a partir de una imagen.

### 6. **docker run -d [nombre_imagen]**
   - **Descripción**: Ejecuta un contenedor en modo "desacoplado" (en segundo plano).

### 7. **docker run -it [nombre_imagen] /bin/bash**
   - **Descripción**: Crea y ejecuta un contenedor en modo interactivo y te proporciona acceso a la consola bash del contenedor.

### 8. **docker ps**
   - **Descripción**: Muestra una lista de los contenedores que están actualmente en ejecución.

### 9. **docker ps -a**
   - **Descripción**: Muestra una lista de todos los contenedores, incluso los detenidos.

### 10. **docker stop [id_contenedor]**
   - **Descripción**: Detiene un contenedor en ejecución.

### 11. **docker start [id_contenedor]**
   - **Descripción**: Inicia un contenedor previamente detenido.

### 12. **docker restart [id_contenedor]**
   - **Descripción**: Reinicia un contenedor en ejecución o detenido.

### 13. **docker rm [id_contenedor]**
   - **Descripción**: Elimina un contenedor detenido.

### 14. **docker logs [id_contenedor]**
   - **Descripción**: Muestra los logs (registros) de un contenedor.

### 15. **docker exec -it [id_contenedor] /bin/bash**
   - **Descripción**: Ejecuta un comando en un contenedor que ya está en ejecución (abre una terminal dentro del contenedor).

### 16. **docker build -t [nombre_imagen] .**
   - **Descripción**: Crea una nueva imagen de Docker a partir de un Dockerfile en el directorio actual.

### 17. **docker inspect [id_contenedor]**
   - **Descripción**: Muestra información detallada sobre un contenedor o una imagen.

### 18. **docker network ls**
   - **Descripción**: Muestra una lista de todas las redes de Docker.

### 19. **docker network create [nombre_red]**
   - **Descripción**: Crea una nueva red personalizada para conectar contenedores.

### 20. **docker network connect [nombre_red] [id_contenedor]**
   - **Descripción**: Conecta un contenedor a una red existente.

### 21. **docker volume ls**
   - **Descripción**: Muestra una lista de los volúmenes de Docker.

### 22. **docker volume create [nombre_volumen]**
   - **Descripción**: Crea un nuevo volumen para el almacenamiento persistente.

### 23. **docker-compose up**
   - **Descripción**: Levanta todos los servicios definidos en un archivo `docker-compose.yml`.

### 24. **docker-compose down**
   - **Descripción**: Detiene y elimina los contenedores y redes creados por Docker Compose.

### 25. **docker save -o [archivo.tar] [nombre_imagen]**
   - **Descripción**: Guarda una imagen de Docker en un archivo tar.

### 26. **docker load -i [archivo.tar]**
   - **Descripción**: Carga una imagen de Docker desde un archivo tar.

### 27. **docker tag [imagen] [registro/nombre_imagen:etiqueta]**
   - **Descripción**: Asigna una etiqueta a una imagen para subirla a un registro de Docker.

### 28. **docker push [registro/nombre_imagen:etiqueta]**
   - **Descripción**: Sube una imagen a un registro de Docker (como Docker Hub).

### 29. **docker export [id_contenedor] > [archivo.tar]**
   - **Descripción**: Exporta el sistema de archivos de un contenedor en ejecución a un archivo tar.

### 30. **docker import [archivo.tar]**
   - **Descripción**: Crea una imagen de Docker desde un archivo tar.
