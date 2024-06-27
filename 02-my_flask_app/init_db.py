import psycopg2

conn = psycopg2.connect(host="db", database="mydatabase", user="myuser", password="mypassword")
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

conn.commit()
cur.close()
conn.close()