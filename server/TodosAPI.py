from flask import Blueprint, jsonify, request
from sql_alchemy_db_instance import db
from models import Todo

todos_api = Blueprint('todos_api', __name__)

@todos_api.route('/todos', methods=['GET'])
def serve_all_todos():
    todo_instances = db.session.query(Todo).all()
    todo_items = [{"id": todo.id, "item": todo.item, "done": todo.done} for todo in todo_instances]
    return jsonify({"items": todo_items})

@todos_api.route('/todo', methods=['POST'])
def add_todo():
    new_todo = Todo()
    new_todo.item = request.json["item"]
    new_todo.done = False
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(success=True)

@todos_api.route('/todo', methods=['PATCH'])
def toggle_done():
    todo_id = request.json["id"]
    target_todo = db.session.query(Todo).filter_by(id=todo_id).first()
    target_todo.done = not target_todo.done
    db.session.add(target_todo)
    db.session.commit()
    return jsonify(success=True)