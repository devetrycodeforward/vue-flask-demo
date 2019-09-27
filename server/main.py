from app import app
from flask import render_template

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
