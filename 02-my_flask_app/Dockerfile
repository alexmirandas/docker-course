FROM python:3.9-slim

# Instala bash
RUN apt-get update && apt-get install -y bash

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
