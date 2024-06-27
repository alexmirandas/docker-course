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