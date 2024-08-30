import os
import subprocess

def scan_folder(path):
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
