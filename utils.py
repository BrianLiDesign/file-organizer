import os


def get_extension(file: str) -> str:
    """
    Returns the file extension of the given file.
    """
    return os.path.splitext(file)[1].lower() or "no_extension"

def is_valid_directory(path: str) -> bool:
    """
    Checks if the given path is a valid directory.
    """
    return os.path.isdir(path)