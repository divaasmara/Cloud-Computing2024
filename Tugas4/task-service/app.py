from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector

app = Flask(__name__)
api = Api(app)

db = mysql.connector.connect(
    host="db",
    user="root",
    password="example",
    database="tasks"
)


class Task(Resource):
    def get(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        return tasks

    def post(self):
        task = request.json['task']
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        db.commit()
        return {'task': task}, 201


api.add_resource(Task, '/tasks')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
