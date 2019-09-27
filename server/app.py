from flask import Flask, render_template, jsonify

todos = ['Study Vue', 'Study Flask', 'Study Toy Problems']

app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
)

@app.route('/')
def serve_vue_app():
    """
    Server our vue app
    """
    return(render_template('index.html'))


@app.route('/todos', methods=['GET'])
def serve_all_todos():
    return jsonify({"items": todos})

@app.after_request
def add_header(req):
    """
    Clear Cache for hot-reloading
    """
    req.headers["Cache-Control"] = "no-cache"
    return req




if __name__ == "__main__":
    app.run(debug=True)
