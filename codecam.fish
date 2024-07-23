#!/usr/bin/env fish

# get dir of currently executing script
set script_dir (dirname (status --current-filename))

# Activate the virtual environment if needed
source $script_dir/venv/bin/activate.fish

# Run the Flask app with the given path
python $script_dir/app.py "$argv[1]"