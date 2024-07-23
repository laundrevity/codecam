from flask import Flask, render_template, request, jsonify
import os
import sys
import webbrowser

app = Flask(__name__)

default_path = "."


@app.route("/")
def index():
    return render_template("index.html", default_path=default_path)


@app.route("/browse", methods=["POST"])
def browse():
    path = request.json.get("path", default_path)
    print(f"{path=}")

    if not path:
        path = "."

    files = []
    for root, dirs, filenames in os.walk(path):
        # Exclude specific directories
        dirs[:] = [d for d in dirs if d not in ["venv", "__pycache__", ".git"]]
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return jsonify(files=files)


@app.route("/generate", methods=["POST"])
def generate():
    files = request.json.get("files", [])
    result = ""
    for file in files:
        with open(file, "r") as f:
            content = f.read()
        result += f"--- {file} ---\n{content}\n\n"
    return jsonify(result=result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        default_path = sys.argv[1]
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
