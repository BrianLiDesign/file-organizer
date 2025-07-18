# File: organizer.py
# Author: Brian Li
# Description: Organizes files into folders based on their extensions.

import os
import shutil
from config import destinations
from utils import get_extension


def categorize(extension: str) -> str:
    """
    Categorizes the file based on its extension.
    If the extension is not found in any category, it returns "Miscellaneous".
    """
    for category, exts in destinations.items():
        if extension in exts:
            return category
    return "Miscellaneous"

def organize_files(path: str):
    """
    Organizes files in the specified directory into subdirectories based on their extensions.
    If the directory does not exist, raises a ValueError.
    
    Parameters:
    - path (str): The path to the directory to organize.
    
    Preconditions:
    - The path must be a valid directory.

    Postconditions:
    - Files are moved into subdirectories named after their categories based on file extensions.
    """
    if not os.path.exists(path):
        raise ValueError(f"'{path}' is not a valid directory.")
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if not os.path.isfile(file_path):
            continue

        ext = get_extension(file)
        folder_name = categorize(ext)
        dest_folder = os.path.join(path, folder_name)

        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, file))
        print(f"Moved {file} → {folder_name}/")