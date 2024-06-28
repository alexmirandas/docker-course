Construir y desplegar una aplicación web en Go (Golang) que se conecte a una base de datos PostgreSQL.

### 1. Preparar la Aplicación en Go

Primero, crea una aplicación en Go que se conecte a PostgreSQL y permita almacenar y consultar registros de una lista de tareas.

#### 1.1. Crear el archivo `main.go`

```go
package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	_ "github.com/lib/pq"
)

var db *sql.DB

type Task struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	Done bool   `json:"done"`
}

func main() {
	var err error
	connStr := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
		os.Getenv("DB_HOST"), os.Getenv("DB_PORT"), os.Getenv("DB_USER"), os.Getenv("DB_PASSWORD"), os.Getenv("DB_NAME"))
	db, err = sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}

	http.HandleFunc("/tasks", handleTasks)
	http.HandleFunc("/tasks/", handleTask)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleTasks(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case "GET":
		rows, err := db.Query("SELECT id, name, done FROM tasks")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		defer rows.Close()

		var tasks []Task
		for rows.Next() {
			var task Task
			if err := rows.Scan(&task.ID, &task.Name, &task.Done); err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			tasks = append(tasks, task)
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(tasks)

	case "POST":
		var task Task
		if err := json.NewDecoder(r.Body).Decode(&task); err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}

		err := db.QueryRow("INSERT INTO tasks(name, done) VALUES($1, $2) RETURNING id", task.Name, task.Done).Scan(&task.ID)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(task)
	}
}

func handleTask(w http.ResponseWriter, r *http.Request) {
	// Similar to handleTasks but for individual task operations
}
```

#### 1.2. Crear el archivo `Dockerfile`

```Dockerfile
FROM golang:1.18-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY *.go ./

RUN go build -o /docker-golang-app

EXPOSE 8080

CMD [ "/docker-golang-app" ]
```

### 2. Inicializar go moduls

#### 2.1. Crear el archivo `go.mod`

```go
module docker-golang-app

go 1.18

require (
	github.com/lib/pq v1.10.2
)
```

#### 2.2. Crea el archivo go.sum
```bash
go mod init docker-golang-app
```

### 3. Crear la Base de Datos

#### 3.1. Crear el archivo `init.sql`

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    done BOOLEAN NOT NULL DEFAULT FALSE
);
```

#### 3.2. Crear el archivo `docker-compose.yml`
```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: tasks_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

  web:
    build: .
    ports:
      - "8080:8080"
    environment:
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: user
      DB_PASSWORD: password
      DB_NAME: tasks_db
    depends_on:
      - db

volumes:
  postgres_data:
```

### 4. Construir y Desplegar la Aplicación

#### 4.1. Ejecutar Docker Compose

```sh
docker-compose up --build -d
```

Esto construirá la imagen de la aplicación Go, iniciará un contenedor PostgreSQL y la aplicación web Go conectada a la base de datos. 

### 5. Probar la Aplicación

Puedes probar la aplicación utilizando `curl` o Postman para hacer peticiones `GET` y `POST` a `http://localhost:8080/tasks`.

#### Ejemplo de petición POST para agregar una tarea:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"name": "Tarea de ejemplo", "done": false}' http://localhost:8080/tasks
```

#### Ejemplo de petición GET para obtener todas las tareas:

```sh
curl http://localhost:8080/tasks
```

Esto debería darte una base sólida para comenzar a construir y desplegar aplicaciones web en Go con PostgreSQL utilizando Docker.