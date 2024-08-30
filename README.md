# Ollama-Model-Dumper

### Export and Backup your Ollama models

<p align="left">
<img src="https://github.com/user-attachments/assets/7e961393-5f2c-4a0b-afc5-57f49b0a490f" height="300">
</p>

---

#### ✨ Check out my other project: [Waifu2x-Extension-GUI](https://github.com/AaronFeng753/Waifu2x-Extension-GUI)

#### Photo/Video/GIF enlargement and Video frame interpolation using machine learning

#### Supports AMD / Nvidia / Intel GPU

---

#### ⭐ Make sure you already installed Python on your PC ⭐

# Export one model:

Download [Export_Model.py](https://github.com/AaronFeng753/Ollama-Model-Dumper/blob/main/Export_Model.py) 

Edit `BackUp_Folder` and `Ollama_Model_Folder` at the bottom of the file:
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

Then start Export_Model.py, enter the model name then click `Enter` key to start export the model.

---

#### ⭐ Make sure you already installed Python on your PC ⭐

# Backup ALL your models:

Download [Backup_ALL_Models.py](https://github.com/AaronFeng753/Ollama-Model-Dumper/blob/main/Backup_ALL_Models.py)

Edit `BackUp_Folder` and `Ollama_Model_Folder` at the bottom of the file:
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

Then start Backup_ALL_Models.py, it will strating to back up all of your models
