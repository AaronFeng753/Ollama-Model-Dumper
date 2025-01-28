import os
import subprocess

def scan_folder(path):
    """
    Scans the given folder path for files with the '.gguf' extension and executes a command to import models.

    Args:
        path (str): The path of the folder to scan.

    The function walks through the directory tree rooted at the given path. For each directory, if any file with the '.gguf' extension is found, it extracts the folder name and prints a message indicating the import of the model. It then constructs and runs a command to import the model using the 'ollama create' command.

    Note:
        - The function uses the 'os.walk' method to traverse the directory tree.
        - The 'subprocess.run' method is used to execute the command.
        - The command is executed in the directory where the '.gguf' file is found.
    """
    # Traverse the directory tree rooted at the given path
        # Check if any file in the current directory ends with '.gguf'
            # Extract the folder name from the current directory path
            # Print a message indicating the import of the model
            # Construct the command to import the model
            # Execute the command in the current directory
    for root, dirs, files in os.walk(path):
        if any(file.endswith('.gguf') for file in files):
            folder_name = os.path.basename(root)
            print(fr'Import model: {folder_name}')
            cmd = f'ollama create {folder_name} -f modelfile'
            subprocess.run(cmd, shell=True, cwd=root)

#****************************************************************
#****************************************************************
#****************************************************************

# Your model backup folder:

scan_folder(r'E:\llama_backup')

#****************************************************************
#****************************************************************
#****************************************************************
