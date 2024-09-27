FROM mkurkcu/javac

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app
RUN javac HelloWorld.java

# Define el comando para ejecutar la aplicación
CMD ["java", "HelloWorld"]