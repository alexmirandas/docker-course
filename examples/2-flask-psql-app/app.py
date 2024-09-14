from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        return jsonify([{'id': task.id, 'name': task.name, 'done': task.done} for task in tasks])
    elif request.method == 'POST':
        data = request.get_json()
        new_task = Task(name=data['name'], done=data['done'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'id': new_task.id, 'name': new_task.name, 'done': new_task.done})

@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'GET':
        return jsonify({'id': task.id, 'name': task.name, 'done': task.done})
    elif request.method == 'PUT':
        data = request.get_json()
        task.name = data['name']
        task.done = data['done']
        db.session.commit()
        return jsonify({'id': task.id, 'name': task.name, 'done': task.done})
    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=8080)
