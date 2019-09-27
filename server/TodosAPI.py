from flask import Blueprint, jsonify, request

todos = [{"item": "Study SQL", "id": 0, "done": False }]

todos_api = Blueprint('todos_api', __name__)


@todos_api.route('/todos', methods=['GET'])
def serve_all_todos():
    return jsonify({"items": todos})

@todos_api.route('/todo', methods=['POST'])
def add_todo():
    todos.append({"item": request.json["item"], "id": 0, "done": False })
    print(todos)
    return jsonify(success=True)