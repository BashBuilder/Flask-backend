from flask import Flask, make_response, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    value1 = "Hello, World!"
    value2 = "Welcome to my Flask app."
    return render_template("index.html", value1=value1, value2=value2)


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
    response = make_response()
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response.data = f'{{"greeting": "{greeting}", "name": "{name}"}}'
    # response.header["Content-Type"] = "text/plain"
    # response.json = {"greeting": greeting, "name": name}

    return response


@app.route("/post", methods=["POST"])
def allow_post():
    data = request.get_json()
    if not data:
        return "No JSON data provided", 400
    return f"Received JSON data: {data}", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
