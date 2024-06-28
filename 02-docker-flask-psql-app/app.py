from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host="db", database="mydatabase", user="myuser", password="mypassword")
    return conn

@app.route('/')
def home():
    return "¡Hola, Docker con PostgreSQL!"

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    name = data['name']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO entries (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Entry added"}), 201

@app.route('/entries', methods=['GET'])
def get_entries():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM entries')
    entries = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
