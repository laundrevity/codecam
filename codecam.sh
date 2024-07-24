#!/bin/bash

# Activate the virtual environment if needed
source "$(dirname "$0")/venv/bin/activate"

# Run the Flask app with the given path
python "$(dirname "$0")/app.py" "$1"
