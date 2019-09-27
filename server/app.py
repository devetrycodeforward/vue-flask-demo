import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from TodosAPI import todos_api, Todo
from sqlAlchemy_db_instance import db


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
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "vue-flask-todos.db"))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(todos_api)
    
    @app.route('/')
    def serve_vue_app():
        """
        Server our vue app
        """
        return(render_template('index.html'))


    @app.after_request
    def add_header(req):
        """
        Clear Cache for hot-reloading
        """
        req.headers["Cache-Control"] = "no-cache"
        return req

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    setup_database(app)
    app.run(debug=True)