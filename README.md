# CodeCam

CodeCam is a tool designed to generate text representations of project files, making it easier to share code snippets and files, especially for collaboration with large language models. This tool can be invoked from the shell and supports multiple shell environments (Fish, Bash, Zsh).

## Features

- Browse and select files from the local filesystem.
- Generate text representations of selected files.
- Supports Fish, Bash, and Zsh shells.
- Automatically opens a web browser to the tool's interface.

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/codecam.git
cd codecam
```

### Create a virtual environment 

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Make the scripts executable
```bash
chmod +x cam codecam.sh codecam.fish
```

### Add CodeCam to Your PATH

To use the `codecam` command from any directory, you need to add the CodeCam directory to your PATH.

#### For Bash/Zsh (Linux/OSX)

1. Open your shell configuration file (`~/.bashrc` or `~/.zshrc`):

    ```bash
    nano ~/.bashrc
    ```

    or

    ```bash
    nano ~/.zshrc
    ```

2. Add the following line to the file:

    ```bash
    export PATH=$PATH:/path/to/your/codecam
    ```

3. Save the file and reload the configuration:

    ```bash
    source ~/.bashrc
    ```

    or

    ```bash
    source ~/.zshrc
    ```

#### For Fish (Linux/OSX)

1. Open your Fish configuration file (`~/.config/fish/config.fish`):

    ```fish
    nano ~/.config/fish/config.fish
    ```

2. Add the following line to the file:

    ```fish
    set -gx PATH /path/to/your/codecam $PATH
    ```

3. Save the file and reload the configuration:

    ```fish
    source ~/.config/fish/config.fish
    ```


## Usage

To use CodeCam, navigate to any project directory and run:

```bash
cam .
```
This command will start the Flask application and open a web browser to the CodeCam interface.