#!/usr/bin/env fish

# Get the directory of the currently executing script
set script_dir (dirname (status --current-filename))

# Create the virtual environment if it doesn't exist
if not test -d "$script_dir/venv"
    python3 -m venv "$script_dir/venv"
    source "$script_dir/venv/bin/activate.fish"
    pip install -r "$script_dir/requirements.txt"
else
    # Activate the virtual environment if it exists
    source $script_dir/venv/bin/activate.fish
end

# Run the Flask app with the given path
python $script_dir/app.py "$argv[1]"
