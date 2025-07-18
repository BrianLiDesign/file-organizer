# File: main.py
# Author: Brian Li
# Project: File Organizer
# Description: Runs the program.

from organizer import organize_files


def main():
    path = input("Enter the path to the folder you want to organize: ")
    try: 
        organize_files(path)
        print("Files organized successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()