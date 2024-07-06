import os
import sys
import logging
from PIL import Image
from imghdr import what
from shutil import copyfile
from tkinter import messagebox, Tk


console_mode = False

def is_console():
    """
    Check if the application is running in a console environment.

    Returns:
    bool: True if running in a console (and bundled with PyInstaller), False otherwise.
    """
    if getattr(sys, 'frozen', False):
        if hasattr(sys.stdout, 'fileno'):
            return True  # It's a console application

    return False

def check_jpeg(filename):
    """
    Check if a file is a JPEG image.

    Args:
    filename (str): The path to the file to be checked.

    Returns:
    bool: True if the file is a JPEG image, False otherwise.
    """
    if os.path.isdir(filename):
        return False

    try:
        image_type = what(filename)
    except (FileNotFoundError, PermissionError, IOError) as e:
        logging.error(f"Error: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False

    if not image_type:
        return False

    return image_type.lower() == 'jpeg'

def save_jpeg(filename):
    """
    Save a JPEG image after creating a backup.

    Args:
    filename (str): The path to the JPEG image file.

    Returns:
    int: 1 if successful, 0 otherwise.
    """
    try:
        with Image.open(filename) as im:
            backup_filename = filename + ".bak"
            copyfile(filename, backup_filename)
            im.save(filename)

            if os.path.exists(backup_filename):
                os.remove(backup_filename)

    except (FileNotFoundError, PermissionError, IsADirectoryError, IOError) as e:
        logging.error(f"Error: {e}")
        return 0
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return 0

    return 1

def convert_files(lst):
    """
    Fix a list of JPEG files to JPEG format.

    Args:
    lst (list): List of file paths to be converted.

    Returns:
    tuple: A tuple containing the number of successfully converted files and the total number of files.
    """
    converted = 0
    total = len(lst)
    for f in lst:
        if check_jpeg(f):
            converted += save_jpeg(f)

    return converted, total

def convert_directory(dir_name):
    """
    Convert all JPEG files in a directory to JPEG format.

    Args:
    dir_name (str): The path to the directory containing files to be converted.

    Returns:
    tuple: A tuple containing the number of successfully converted files and the total number of files processed.
    """
    try:
        files_list = os.listdir(dir_name)
        files_list = [os.path.join(dir_name, file) for file in files_list]
        return convert_files(files_list)
    except (FileNotFoundError, PermissionError, OSError) as e:
        logging.error(f"Error: {e}")
        return 0
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return 0

def show_message(title, message):
    """
    Show a message box with title and message.

    Args:
    title (str): Title of the message box.
    message (str): Message to be displayed.

    Returns:
    None
    """
    global console_mode
    if console_mode:
        return
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, message)

def main():
    global console_mode
    console_mode = is_console()

    argc = len(sys.argv)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)

    if argc < 2:
        print("Wazzap - Fix WhatsApp JPEG images for Photoshop\n")
        print("Usage:")
        print("\tWazzapp im1.jpg [im2.jpeg ...]")
        print("\tWazzapp directory")
        show_message("Wazzap - Fix WhatsApp JPEG images for Photoshop", "Add at least one JPEG file as an argument")
        sys.exit(0)

    converted, total = 0, 0
    if argc == 2 and os.path.isdir(sys.argv[1]):
        converted, total = convert_directory(sys.argv[1])
    else:
        converted, total = convert_files(sys.argv[1:])

    message = f"Converted {converted}/{total} files"
    print(message)
    show_message("Wazzap - Finished", message)

if __name__ == "__main__":
    main()