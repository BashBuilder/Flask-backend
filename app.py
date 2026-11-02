from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/greet/<name>")
def greet(name: str):
    return f"Hello, {name}!"


@app.route("/add/<int:a>/<int:b>")
def add(a: int, b: int):
    return str(a + b)


@app.route("/params")
def handle_params():
    greeting = request.args.get("greeting", "Hello")
    name = request.args.get("name", "World")
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
