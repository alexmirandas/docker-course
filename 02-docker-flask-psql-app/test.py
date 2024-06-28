import psycopg2

try:
    conn = psycopg2.connect(host="db", database="mydatabase", user="myuser", password="mypassword")
    print("Conexión exitosa")
except Exception as e:
    print(f"Error al conectar: {e}")

