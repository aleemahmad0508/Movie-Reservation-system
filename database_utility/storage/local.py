import os
import shutil

def save_locally(file_path):
    os.makedirs("backups",exist_ok=True)
    destination=os.path.join("backups",os.path.basename(file_path))
    shutil.move(file_path,destination)

    return destination