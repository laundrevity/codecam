from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/browse", methods=["POST"])
def browse():
    path = request.json.get("path")
    if not path:
        path = "."
    files = []
    for root, dirs, filenames in os.walk(path):
        # exclude specific dirs
        dirs[:] = [d for d in dirs if d not in ["venv", "__pycache__", ".git"]]
        for filename in filenames:
            files.append(os.path.join(root, filename))

    print(f"{files=}")

    return jsonify(files=files)


@app.route("/generate", methods=["POST"])
def generate():
    files = request.json.get("files")
    result = ""
    for file in files:
        with open(file, "r") as f:
            content = f.read()
        result += f"--- {file} ---\n{content}\n\n"
    return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)
