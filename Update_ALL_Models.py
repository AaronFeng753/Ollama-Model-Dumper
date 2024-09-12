# This Python script utilizes the pull command of ollama to simultaneously update all models downloaded from ollama.com

import subprocess
import re
import os
import shutil

def run_command(command):
    """
    Executes a shell command and returns the output.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW, encoding='utf-8')

    # Capture the output and error
    output_text, error_text = process.communicate()

    # Trim the output text
    return output_text.strip()

def process_models(model_names):
    for model_name in model_names:
        model_name = model_name.strip()
        print(model_name)
        parameters_command = f'ollama pull {model_name}'
        subprocess.run(parameters_command, shell=True)

def extract_names(data):
    lines = data.strip().split('\n')
    names = [line.split()[0] for line in lines[1:]]
    return ';;;'.join(names)

data = run_command("ollama list")
# Call the function and print the result
model_names_string = extract_names(data)
model_names = model_names_string.split(";;;")
process_models(model_names)
