from flask import Flask, render_template
from TodosAPI import todos_api

app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
)

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


if __name__ == "__main__":
    app.run(debug=True)
