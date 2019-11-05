import os
from flask import Flask, render_template
from TodosAPI import todos_api, Todo
from sql_alchemy_db_instance import db


project_dir = os.path.dirname(os.path.abspath(__file__))
project_paths = project_dir.split("/")
project_paths.pop()
project_paths.append('db')
project_dir = "/".join(project_paths)

def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(user=os.environ["DB_USER"],pw=os.environ["DB_PASS"],url=os.environ["DB_URL"],db=os.environ["DB_NAME"])
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(todos_api)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()