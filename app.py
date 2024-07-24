from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
import sys
import json
import shutil
import platform
import subprocess
import webbrowser

app = Flask(__name__)

default_path = "."
selected_files_path = "selected_files.json"


@app.route("/")
def index():
    # Load previously selected files
    if os.path.exists(selected_files_path):
        with open(selected_files_path, "r") as f:
            selected_files = json.load(f)
    else:
        selected_files = []
    return render_template(
        "index.html", default_path=default_path, selected_files=selected_files
    )


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
    result = generate_snapshot(files)

    # Save the selected files
    with open(selected_files_path, "w") as f:
        json.dump(files, f)

    return jsonify(result=result)


@app.route("/clone", methods=["POST"])
def clone_repo():
    repo_url = request.json.get("repo_url")
    clone_dir = request.json.get("clone_dir", "cloned_repo")

    if os.path.exists(clone_dir):
        return jsonify(
            {"stdout": "Repo already exists.", "stderr": "Repo already exists."}
        )

    result = subprocess.run(
        ["git", "clone", repo_url, clone_dir], capture_output=True, text=True
    )

    if result.returncode == 0:
        stdout = f"Repository cloned successfully to {clone_dir}."
        stderr = None
    else:
        print(f"{result.stdout=}, {result.stderr=}")
        stdout = "Failed to clone repository."
        stderr = result.stderr

    return jsonify({"stdout": stdout, "stderr": stderr})


def generate_snapshot(files=None):
    if files is None:
        if os.path.exists(selected_files_path):
            with open(selected_files_path, "r") as f:
                files = json.load(f)
        else:
            return None

    system_info = (
        f"System: {platform.system()} {platform.release()} {platform.version()}"
    )
    result = f"{system_info}\nTime: {datetime.now()}\n"
    for file in files:
        with open(file, "r") as f:
            content = f.read()
        result += f"--- {file} ---\n{content}\n\n"

    return result


def copy_to_clipboard(text):
    if platform.system() == "Darwin":
        subprocess.run("pbcopy", text=True, input=text)
    elif platform.system() == "Linux":
        if shutil.which("xclip") is not None:
            subprocess.run(["xclip", "-selection", "clipboard"], text=True, input=text)
        else:
            print(
                "xclip is not installed. Please install xclip to use this feature on Linux, e.g. via `sudo apt install xclip`."
            )
    elif platform.system() == "Windows":
        subprocess.run("clip", text=True, input=text)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gen":
        snapshot = generate_snapshot()
        if snapshot:
            copy_to_clipboard(snapshot)
        else:
            print("No selected files found.")
    else:

        if platform.system() == "Linux" and "Microsoft" in platform.uname().release:
            # WSL-specific command to open the browser
            os.system("powershell.exe Start-Process http://127.0.0.1:5000")
        else:
            webbrowser.open("http://127.0.0.1:5000")

        app.run()
