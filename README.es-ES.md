

# Ollama-Model-Dumper 🦙

### Exporta y haz copias de seguridad de tus modelos de Ollama a formatos GGUF y ModelFile

<p align="left">
<img src="https://github.com/user-attachments/assets/7e961393-5f2c-4a0b-afc5-57f49b0a490f" height="300">
</p>

### 📜 Cómo usar: 
- [Exportar un modelo](https://github.com/AaronFeng753/Ollama-Model-Dumper#export-one-model)
- [Hacer copia de seguridad de TODOS tus modelos](https://github.com/AaronFeng753/Ollama-Model-Dumper#backup-all-your-models)
- [Importar tu carpeta de respaldo a Ollama](https://github.com/AaronFeng753/Ollama-Model-Dumper#import-your-backup-folder-into-ollama)
- [Actualizar tus modelos de Ollama](https://github.com/AaronFeng753/Ollama-Model-Dumper/blob/main/README.md#update-your-ollama-models)

### ⚠️ Aviso:
```
I have only tested these two scripts on Windows 11 + Ollama 0.3.8
I am not sure if they will work correctly on Mac or Linux systems.
This is just a free open-source script, I am not responsible for any consequences that may arise from your use of the code.
```

---

### ✨ Echa un vistazo a mi otro proyecto: [Waifu2x-Extension-GUI](https://github.com/AaronFeng753/Waifu2x-Extension-GUI)

#### Aumento de tamaño de fotos/videos/GIFs e interpolación de cuadros de video mediante aprendizaje automático

#### Compatible con GPUs AMD / Nvidia / Intel

---

#### ⭐ Asegúrate de tener Python instalado en tu PC ⭐

# Exportar un modelo:

Descarga [Export_Model.py](https://github.com/AaronFeng753/Ollama-Model-Dumper/blob/main/Export_Model.py) 

Edita `BackUp_Folder` y `Ollama_Model_Folder` en la parte inferior del archivo:
```
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
model_name = input("Enter model name: ")
```

Luego inicia Export_Model.py, introduce el nombre del modelo y pulsa la tecla `Enter` para comenzar a exportar el modelo.

Hará una copia de seguridad de los archivos gguf y modelfile en una carpeta:

<p align="left">
<img src="https://github.com/user-attachments/assets/70083bea-575c-4b7f-b4f1-affb950b2286" height="80">
<img src="https://github.com/user-attachments/assets/c317203a-3b87-45c6-8d7d-a2b79bd10625" height="80">
</p>


---

#### ⭐ Asegúrate de tener Python instalado en tu PC ⭐

# Hacer copia de seguridad de TODOS tus modelos:

Descarga [Backup_ALL_Models.py](https://github.com/AaronFeng753/Ollama-Model-Dumper/blob/main/Backup_ALL_Models.py)

Edita `BackUp_Folder` y `Ollama_Model_Folder` en la parte inferior del archivo:
```
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
```

Luego inicia Backup_ALL_Models.py, comenzará a hacer una copia de seguridad de todos tus modelos

Hará una copia de seguridad de los archivos gguf y modelfile en una carpeta:

<p align="left">
<img src="https://github.com/user-attachments/assets/d2e5835b-bdea-4014-92b5-3c8aaca08aea" height="200">
<img src="https://github.com/user-attachments/assets/c317203a-3b87-45c6-8d7d-a2b79bd10625" height="80">
</p>

Para evitar copias innecesarias, de forma predeterminada omitirá el modelo si ya existe en la carpeta de respaldo

Puedes desactivar esta función eliminando 

```
    if os.path.exists(new_folder_path) and os.path.isdir(new_folder_path):
        print(f"Model: '{model_name}' already exists in the backup folder, so it will be skipped.")
        return
```

En:

```
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
```

---

#### ⭐ Asegúrate de tener Python instalado en tu PC ⭐

# Importar tu carpeta de respaldo a Ollama:

Descarga [Import_Models.py](https://github.com/AaronFeng753/Ollama-Model-Dumper/blob/main/Import_Models.py)

Edita `scan_folder` en la parte inferior del archivo:
```
#****************************************************************

# Your model backup folder:

scan_folder(r'E:\llama_backup')

#****************************************************************
```

Luego inicia Import_Models.py, comenzará a importar todas tus copias de seguridad de modelos a Ollama

---

#### ⭐ Asegúrate de tener Python instalado en tu PC ⭐

# Actualizar tus modelos de Ollama:

Descarga: [Update_ALL_Models.py](https://github.com/AaronFeng753/Ollama-Model-Dumper/blob/main/Update_ALL_Models.py)

Luego inicia Update_ALL_Models.py, comenzará a actualizar todos tus modelos de Ollama utilizando el comando pull de Ollama.

Solo se actualizarán los modelos que hayas descargado desde ollama.com.

---

### ✨ Echa un vistazo a mi otro proyecto: [Waifu2x-Extension-GUI](https://github.com/AaronFeng753/Waifu2x-Extension-GUI)

#### Aumento de tamaño de fotos/videos/GIFs e interpolación de cuadros de video mediante aprendizaje automático

#### Compatible con GPUs AMD / Nvidia / Intel

![](https://raw.githubusercontent.com/AaronFeng753/AaronFeng753/main/res/ReadMeCover.png)
