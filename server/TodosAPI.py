from flask import Blueprint, jsonify, request

todos = ['Study Vue', 'Study Flask', 'Study Toy Problems']

todos_api = Blueprint('todos_api', __name__)


@todos_api.route('/todos', methods=['GET'])
def serve_all_todos():
    return jsonify({"items": todos})

@todos_api.route('/todo', methods=['POST'])
def add_todo():
    todos.append(request.json["item"])
    print(todos)
    return jsonify(success=True)