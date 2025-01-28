import subprocess
import re
import os
import shutil

def sanitize_filename_MF(name):
    name = name.replace(":latest","")
    return re.sub(r'[<>:"/\\|?*.]', '-', name)

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW, encoding='utf-8')

    output_text, error_text = process.communicate()

    return output_text.strip()

def create_ollama_model_file(model_name, output_file, BackUp_Folder, Ollama_Model_Folder):
    """
    Creates a backup of an Ollama model by generating a model file with its template, parameters, and system messages.
    Args:
        model_name (str): The name of the Ollama model to back up.
        output_file (str): The name of the output file to create in the backup folder.
        BackUp_Folder (str): The path to the folder where the backup will be stored.
        Ollama_Model_Folder (str): The path to the folder where the original Ollama models are stored.
    Returns:
        None
    The function performs the following steps:
    1. Retrieves the template, parameters, system message, and model file location of the specified model.
    2. Sanitizes the model name to create a valid folder name.
    3. Checks if a backup folder for the model already exists. If it does, the function skips the backup.
    4. Creates a new folder for the model backup if it does not already exist.
    5. Constructs the content of the model file using the retrieved template, parameters, and system message.
    6. Writes the constructed content to the specified output file in the backup folder.
    7. Extracts the model file location from the retrieved model file message.
    8. Copies and renames the model file to the backup folder if it exists.
    Note:
        The function assumes the existence of helper functions `run_command` and `sanitize_filename_MF`.
        It also uses the `os`, `shutil`, and `re` modules for file operations and regular expressions.
    """
    template_command = f'ollama show --template {model_name}'
    template = run_command(template_command)
    
    if not template:
        print(f"Error: model '{model_name}' not found or the template is empty. Please check the model name and try again.")
        return
    
    parameters_command = f'ollama show --parameters {model_name}'
    parameters = run_command(parameters_command)
    
    system_command = f'ollama show --system {model_name}'
    system_message = run_command(system_command)
    
    modelfile_command = f'ollama show --modelfile {model_name}'
    modelfile_message = run_command(modelfile_command)
    
    model_name = sanitize_filename_MF(model_name)
    
    new_folder_path = os.path.join(BackUp_Folder, model_name)
    
    #****************************************************************
    #****************************************************************
    #****************************************************************
    if os.path.exists(new_folder_path) and os.path.isdir(new_folder_path):
        print(f"Model: '{model_name}' already exists in the backup folder, so it will be skipped.")
        return
    #****************************************************************
    #****************************************************************
    #****************************************************************

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Created folder: {new_folder_path}")
    else:
        print(f"Folder already exists: {new_folder_path}")
    
    model_content = f"""FROM {model_name}.gguf
TEMPLATE """ + '"""' + f"""{template}""" + '"""' + "\n"
    
    for line in parameters.splitlines():
        model_content += f'PARAMETER {line}\n'
    
    model_content += f'system "{system_message}"\n'
    
    print(model_content)
    
    with open(os.path.join(new_folder_path, output_file), 'w', encoding="utf-8") as file:
        file.write(model_content)
    
    print(f'Model file created: {output_file}')
    
    modelfile_message = modelfile_message.strip()
    
    model_file_location_match = re.search(fr'FROM\s+({re.escape(Ollama_Model_Folder)}[^\s]*)', modelfile_message, re.MULTILINE)
    extracted_model_file_location = model_file_location_match.group(1) if model_file_location_match else "Model_file_location_not_found"
    
    print(f"Model gguf file found: {extracted_model_file_location}")
    
    new_model_file_name = f"{model_name}.gguf"
    new_model_file_path = os.path.join(new_folder_path, new_model_file_name)

    if os.path.exists(extracted_model_file_location):
        shutil.copy2(extracted_model_file_location, new_model_file_path)
        print(f"Copied and renamed model file to: {new_model_file_path}")
    else:
        print(f"Model file not found at: {extracted_model_file_location}")

def process_models(model_names):
    for model_name in model_names:
        model_name = model_name.strip()
        print(model_name)
        #output_file = f"Modelfile-{sanitize_filename_MF(model_name)}"
        output_file = f"ModelFile"
        #****************************************************************
        #****************************************************************
        #****************************************************************
        # Your ollama model folder:
        Ollama_Model_Folder = r"D:\llama\.ollama\models"
        
        # Where you want to back up your models:
        BackUp_Folder = r"E:\llama_backup"
        #****************************************************************
        #****************************************************************
        #****************************************************************
        create_ollama_model_file(model_name, output_file, BackUp_Folder, Ollama_Model_Folder)

def extract_names(data):
    lines = data.strip().split('\n')
    names = [line.split()[0] for line in lines[1:]]
    return ';;;'.join(names)

data = run_command("ollama list")
model_names_string = extract_names(data)
model_names = model_names_string.split(";;;")
process_models(model_names)
