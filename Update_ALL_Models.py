# This Python script utilizes the pull command of ollama to simultaneously update all models downloaded from ollama.com

import subprocess
import re
import os
import shutil

def run_command(command):
    """
    Executes a shell command and returns the output.
    Args:
        command (str): The shell command to be executed.
    Returns:
        str: The trimmed output of the executed command.
    Raises:
        subprocess.CalledProcessError: If the command returns a non-zero exit status.
    # Execute the command in a subprocess
   
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW, encoding='utf-8')

    # Capture the output and error
    output_text, error_text = process.communicate()

    # Trim the output text
    return output_text.strip()

def process_models(model_names):
    """
    Processes a list of model names by stripping whitespace and executing a shell command to pull each model.

    Args:
        model_names (list of str): A list of model names to be processed.

    Returns:
        None

    Example:
        model_names = ["model1", "model2", "model3"]
        process_models(model_names)
    """
    # Iterate over each model name in the list
        # Remove leading and trailing whitespace from the model name
        # Print the processed model name
        # Construct the shell command to pull the model
        # Execute the shell command
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
