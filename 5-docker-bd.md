## **Ejercicios con MySQL**

### **Ejercicio 1: Levantar un contenedor MySQL**
1. **Objetivo**: Crear y ejecutar un contenedor de MySQL usando Docker.
2. **Comandos a usar**: `docker run`, `docker exec`, `docker ps`.

   **Instrucciones**:
   - Levanta un contenedor de MySQL especificando una contraseña para el usuario root:
     ```bash
     docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=mi_contraseña -d mysql:latest
     ```
   - Verifica que el contenedor está corriendo:
     ```bash
     docker ps
     ```

---

### **Ejercicio 2: Conectarse a MySQL desde el contenedor**
1. **Objetivo**: Conectar al contenedor MySQL e interactuar con la base de datos.
2. **Comandos a usar**: `docker exec`.

   **Instrucciones**:
   - Conéctate al contenedor y abre el cliente MySQL:
     ```bash
     docker exec -it mysql-container mysql -uroot -p
     ```
   - Crea una base de datos llamada `test_db`:
     ```sql
     CREATE DATABASE test_db;
     ```

---

### **Ejercicio 3: Crear tablas y agregar datos**
1. **Objetivo**: Crear una tabla y agregar datos en una base de datos MySQL dentro de Docker.
2. **Comandos a usar**: `docker exec`, `mysql`.

   **Instrucciones**:
   - Conéctate nuevamente al contenedor MySQL:
     ```bash
     docker exec -it mysql-container mysql -uroot -p
     ```
   - Usa la base de datos `test_db`:
     ```sql
     USE test_db;
     ```
   - Crea una tabla `personas` con los campos `id`, `nombre`, y `edad`:
     ```sql
     CREATE TABLE personas (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(100),
       edad INT
     );
     ```
   - Inserta algunos datos en la tabla:
     ```sql
     INSERT INTO personas (nombre, edad) VALUES ('Juan', 30), ('Ana', 25), ('Luis', 40);
     ```

---

### **Ejercicio 4: Exportar los datos de la base de datos MySQL**
1. **Objetivo**: Realizar un respaldo de la base de datos utilizando `mysqldump`.
2. **Comandos a usar**: `docker exec`, `mysqldump`.

   **Instrucciones**:
   - Realiza un respaldo de la base de datos `test_db`:
     ```bash
     docker exec mysql-container mysqldump -uroot -pmi_contraseña test_db > backup.sql
     ```

---

### **Ejercicio 5: Importar un respaldo a MySQL**
1. **Objetivo**: Restaurar una base de datos en MySQL desde un archivo SQL.
2. **Comandos a usar**: `docker exec`, `mysql`.

   **Instrucciones**:
   - Crea una nueva base de datos `restored_db`:
     ```bash
     docker exec -it mysql-container mysql -uroot -p -e "CREATE DATABASE restored_db;"
     ```
   - Restaura los datos en la nueva base de datos desde el respaldo:
     ```bash
     docker exec -i mysql-container mysql -uroot -pmi_contraseña restored_db < backup.sql
     ```

---

## **Ejercicios con PostgreSQL**

### **Ejercicio 1: Levantar un contenedor de PostgreSQL**
1. **Objetivo**: Crear y ejecutar un contenedor de PostgreSQL usando Docker.
2. **Comandos a usar**: `docker run`, `docker exec`.

   **Instrucciones**:
   - Levanta un contenedor de PostgreSQL especificando un usuario y una contraseña:
     ```bash
     docker run --name postgres-container -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=mi_contraseña -d postgres:latest
     ```

---

### **Ejercicio 2: Conectarse a PostgreSQL desde el contenedor**
1. **Objetivo**: Conectarse al contenedor de PostgreSQL y crear una base de datos.
2. **Comandos a usar**: `docker exec`, `psql`.

   **Instrucciones**:
   - Conéctate al contenedor y abre el cliente `psql`:
     ```bash
     docker exec -it postgres-container psql -U admin
     ```
   - Crea una base de datos llamada `test_db`:
     ```sql
     CREATE DATABASE test_db;
     ```

---

### **Ejercicio 3: Crear tablas y agregar datos**
1. **Objetivo**: Crear una tabla y agregar datos en PostgreSQL dentro de Docker.
2. **Comandos a usar**: `docker exec`, `psql`.

   **Instrucciones**:
   - Conéctate nuevamente al contenedor PostgreSQL y usa la base de datos `test_db`:
     ```bash
     docker exec -it postgres-container psql -U admin -d test_db
     ```
   - Crea una tabla `personas` con los campos `id`, `nombre`, y `edad`:
     ```sql
     CREATE TABLE personas (
       id SERIAL PRIMARY KEY,
       nombre VARCHAR(100),
       edad INT
     );
     ```
   - Inserta algunos datos en la tabla:
     ```sql
     INSERT INTO personas (nombre, edad) VALUES ('Juan', 30), ('Ana', 25), ('Luis', 40);
     ```

---

### **Ejercicio 4: Exportar los datos de la base de datos PostgreSQL**
1. **Objetivo**: Realizar un respaldo de la base de datos utilizando `pg_dump`.
2. **Comandos a usar**: `docker exec`, `pg_dump`.

   **Instrucciones**:
   - Realiza un respaldo de la base de datos `test_db`:
     ```bash
     docker exec postgres-container pg_dump -U admin test_db > backup.sql
     ```

---

### **Ejercicio 5: Importar un respaldo en PostgreSQL**
1. **Objetivo**: Restaurar una base de datos en PostgreSQL desde un archivo SQL.
2. **Comandos a usar**: `docker exec`, `psql`.

   **Instrucciones**:
   - Crea una nueva base de datos `restored_db`:
     ```bash
     docker exec -it postgres-container psql -U admin -c "CREATE DATABASE restored_db;"
     ```
   - Restaura los datos en la nueva base de datos desde el respaldo:
     ```bash
     docker exec -i postgres-container psql -U admin -d restored_db < backup.sql
     ```

---

### **Ejercicio 6: Usar volúmenes para almacenamiento persistente**
1. **Objetivo**: Levantar un contenedor PostgreSQL con almacenamiento persistente usando volúmenes.
2. **Comandos a usar**: `docker run`, `docker volume`.

   **Instrucciones**:
   - Crea un volumen para almacenamiento persistente:
     ```bash
     docker volume create postgres-data
     ```
   - Levanta un contenedor de PostgreSQL usando ese volumen:
     ```bash
     docker run --name postgres-container -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=mi_contraseña -v postgres-data:/var/lib/postgresql/data -d postgres:latest
     ```

---

### **Ejercicio 7: Configurar conexión entre MySQL y PostgreSQL usando Docker Networks**
1. **Objetivo**: Crear una red de Docker para permitir que MySQL y PostgreSQL se comuniquen.
2. **Comandos a usar**: `docker network create`, `docker run`, `docker network connect`.

   **Instrucciones**:
   - Crea una red de Docker:
     ```bash
     docker network create db-network
     ```
   - Conéctate a esta red con los contenedores de MySQL y PostgreSQL:
     ```bash
     docker network connect db-network mysql-container
     docker network connect db-network postgres-container
     ```
