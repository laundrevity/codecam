#!/bin/bash

# Determine the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

# Create the virtual environment if it doesn't exist
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    python3 -m venv "$SCRIPT_DIR/venv"
    source "$SCRIPT_DIR/venv/bin/activate"
    pip install -r "$SCRIPT_DIR/requirements.txt"
else
    # Activate the virtual environment if it exists
    source "$SCRIPT_DIR/venv/bin/activate"
fi

# Run the Flask app with the given path
python "$SCRIPT_DIR/app.py" "$1"
