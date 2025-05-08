import subprocess
import re
import os
import shutil

def sanitize_filename_MF(name):
    name = name.replace(":latest","")
    return re.sub(r'[<>:"/\\|?*.]', '-', name)

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True, encoding='utf-8')

    output_text, error_text = process.communicate()

    return output_text.strip()

def create_ollama_model_file(model_name, output_file, BackUp_Folder, Ollama_Model_Folder):
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
    
    with open(os.path.join(new_folder_path, output_file), 'w') as file:
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

#****************************************************************
#****************************************************************
#****************************************************************
# Your ollama model folder:
Ollama_Model_Folder = r"/usr/share/ollama/.ollama/models"

# Where you want to back up your models:
BackUp_Folder = r"./llama_backup"
#****************************************************************
#****************************************************************
#****************************************************************
model_name = input("Enter model name: ")
model_name = model_name.strip()
#output_file = f"Modelfile-{sanitize_filename_MF(model_name)}"
output_file = f"ModelFile"
create_ollama_model_file(model_name, output_file, BackUp_Folder, Ollama_Model_Folder)
