---

### **Ejercicio 1: Crear una imagen de Python con un script simple**
1. **Objetivo**: Crear una imagen de Docker que ejecute un script de Python al iniciarse.
2. **Instrucciones**:
   - Crea un archivo llamado `app.py` con el siguiente contenido:
     ```python
     print("¡Hola, Docker desde Python!")
     ```
   - Crea un Dockerfile que:
     - Use como base la imagen oficial de Python.
     - Copie el archivo `app.py` al contenedor.
     - Ejecute el script de Python al iniciar el contenedor.

   **Dockerfile**:
   ```Dockerfile
   # Usar la imagen base de Python
   FROM python:3.9-slim

   # Establecer el directorio de trabajo en /app
   WORKDIR /app

   # Copiar el archivo app.py a /app
   COPY app.py .

   # Ejecutar el script de Python
   CMD ["python", "app.py"]
   ```

   - Construye y ejecuta la imagen:
     ```bash
     docker build -t python-app .
     docker run python-app
     ```

---

### **Ejercicio 2: Crear una imagen de Node.js que sirva una aplicación web**
1. **Objetivo**: Crear una imagen de Docker que sirva una aplicación simple de Node.js.
2. **Instrucciones**:
   - Crea un archivo `app.js` con el siguiente contenido:
     ```javascript
     const http = require('http');

     const server = http.createServer((req, res) => {
       res.statusCode = 200;
       res.setHeader('Content-Type', 'text/plain');
       res.end('¡Hola, Docker desde Node.js!\n');
     });

     server.listen(3000, () => {
       console.log('El servidor está escuchando en http://localhost:3000');
     });
     ```

   - Crea un archivo `package.json` con las dependencias:
     ```json
     {
       "name": "node-app",
       "version": "1.0.0",
       "main": "app.js",
       "dependencies": {
         "http": "0.0.1-security"
       }
     }
     ```

   - Crea un Dockerfile que:
     - Use como base la imagen oficial de Node.js.
     - Copie el archivo `package.json` y `app.js` al contenedor.
     - Instale las dependencias y ejecute el servidor.

   **Dockerfile**:
   ```Dockerfile
   # Usar la imagen base de Node.js
   FROM node:14

   # Crear directorio de la app
   WORKDIR /usr/src/app

   # Copiar package.json e instalar dependencias
   COPY package.json .
   RUN npm install

   # Copiar el resto de los archivos
   COPY . .

   # Exponer el puerto 3000
   EXPOSE 3000

   # Comando para ejecutar la app
   CMD ["node", "app.js"]
   ```

   - Construye y ejecuta la imagen:
     ```bash
     docker build -t node-app .
     docker run -p 3000:3000 node-app
     ```

   - Visita `http://localhost:3000` en tu navegador para ver la salida.

---

### **Ejercicio 3: Crear una imagen de Nginx con un archivo HTML personalizado**
1. **Objetivo**: Servir una página HTML personalizada usando un contenedor de Nginx.
2. **Instrucciones**:
   - Crea un archivo `index.html` con contenido personalizado:
     ```html
     <html>
       <head>
         <title>Página de Docker</title>
       </head>
       <body>
         <h1>¡Bienvenido a Docker con Nginx!</h1>
       </body>
     </html>
     ```

   - Crea un Dockerfile que:
     - Use como base la imagen oficial de Nginx.
     - Copie el archivo `index.html` en el directorio de Nginx.

   **Dockerfile**:
   ```Dockerfile
   # Usar la imagen base de Nginx
   FROM nginx:latest

   # Copiar archivo HTML al directorio de Nginx
   COPY index.html /usr/share/nginx/html/index.html

   # Exponer el puerto 80
   EXPOSE 80
   ```

   - Construye y ejecuta la imagen:
     ```bash
     docker build -t custom-nginx .
     docker run -p 8080:80 custom-nginx
     ```

   - Visita `http://localhost:8080` para ver tu página personalizada.

---

### **Ejercicio 4: Crear una imagen de Go con compilación**
1. **Objetivo**: Crear una imagen de Docker que compile y ejecute una aplicación de Go.
2. **Instrucciones**:
   - Crea un archivo `main.go` con el siguiente contenido:
     ```go
     package main

     import "fmt"

     func main() {
         fmt.Println("¡Hola, Docker desde Go!")
     }
     ```

   - Crea un Dockerfile que:
     - Use como base la imagen oficial de Go.
     - Compile el archivo Go.
     - Ejecute el binario resultante.

   **Dockerfile**:
   ```Dockerfile
   # Usar la imagen base de Go
   FROM golang:1.16

   # Establecer el directorio de trabajo
   WORKDIR /app

   # Copiar el archivo main.go
   COPY main.go .

   # Compilar el programa
   RUN go build -o main .

   # Ejecutar el binario compilado
   CMD ["./main"]
   ```

   - Construye y ejecuta la imagen:
     ```bash
     docker build -t go-app .
     docker run go-app
     ```

---

### **Ejercicio 5: Crear una imagen de Python con variables de entorno**
1. **Objetivo**: Crear una imagen que acepte una variable de entorno para personalizar su comportamiento.
2. **Instrucciones**:
   - Crea un archivo `app.py` que lea una variable de entorno:
     ```python
     import os

     name = os.getenv("NAME", "Mundo")
     print(f"¡Hola, {name} desde Docker!")
     ```

   - Crea un Dockerfile que:
     - Use como base la imagen oficial de Python.
     - Ejecute el script `app.py`.

   **Dockerfile**:
   ```Dockerfile
   # Usar la imagen base de Python
   FROM python:3.9-slim

   # Establecer el directorio de trabajo
   WORKDIR /app

   # Copiar el archivo app.py
   COPY app.py .

   # Establecer una variable de entorno por defecto
   ENV NAME Mundo

   # Ejecutar el script de Python
   CMD ["python", "app.py"]
   ```

   - Construye y ejecuta la imagen, pasando una variable de entorno personalizada:
     ```bash
     docker build -t python-env-app .
     docker run -e NAME=Juan python-env-app
     ```

---

### **Ejercicio 6: Imagen multi-etapa para reducir tamaño**
1. **Objetivo**: Crear una imagen usando una compilación multi-etapa para reducir el tamaño de la imagen final.
2. **Instrucciones**:
   - Crea un archivo `app.go` con el siguiente contenido:
     ```go
     package main

     import "fmt"

     func main() {
         fmt.Println("¡Hola, Docker multi-etapa!")
     }
     ```

   - Crea un Dockerfile que use una etapa para compilar y otra para ejecutar:
   **Dockerfile**:
   ```Dockerfile
   # Etapa de construcción
   FROM golang:1.16 AS builder
   WORKDIR /app
   COPY app.go .
   RUN go build -o app .

   # Etapa final
   FROM alpine:latest
   WORKDIR /app
   COPY --from=builder /app/app .
   CMD ["./app"]
   ```

   - Construye y ejecuta la imagen:
     ```bash
     docker build -t multi-stage-app .
     docker run multi-stage-app
     ```

   - Observa que el tamaño de la imagen final es mucho menor al separar la compilación y ejecución en diferentes etapas.

---

### **Ejercicio 7: Crear una imagen con múltiples servicios usando supervisord**
1. **Objetivo**: Crear una imagen que ejecute varios servicios (por ejemplo, Nginx y un servidor SSH) utilizando `supervisord`.
2. **Instrucciones**:
   - Crea un archivo de configuración `supervisord.conf`:
     ```ini
     [supervisord]
     nodaemon=true

     [program:nginx]
     command=/usr/sbin/nginx -g 'daemon off;'

     [program:sshd]
     command=/usr/sbin/sshd -D
     ```

   - Crea un Dockerfile que instale Nginx y SSH, y use supervisord para ejecutar ambos servicios.
   
   **Dockerfile**:
   ```Dockerfile
   FROM ubuntu:20.04

   # Instalar Nginx y SSH
   RUN apt-get update &&

 apt-get install -y nginx openssh-server supervisor

   # Copiar archivo de configuración de supervisord
   COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

   # Exponer los puertos
   EXPOSE 80 22

   # Comando para ejecutar supervisord
   CMD ["/usr/bin/supervisord"]
   ```

   - Construye y ejecuta la imagen:
     ```bash
     docker build -t multi-service-app .
     docker run -p 80:80 -p 2222:22 multi-service-app
     ```
