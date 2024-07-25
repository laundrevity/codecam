import platform
import datetime
import json
import os


def generate_snapshot(selected_files_path, files=None, history_length=10):
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
        if os.path.isdir(file):
            continue
        with open(file, "r") as f:
            content = f.read()
        result += f"--- {file} ---\n{content}\n\n"

    if history_length > 0:
        log_path = os.path.expanduser("~/.command_history_log")
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                log_content = f.read()
            result += f"\n--- Command History Log ---\n{log_content}"

    return result
