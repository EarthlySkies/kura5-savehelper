# A part of the "kura5-savehelper" project found on GitHub
# This is the main library file "savehelper.py" will be utilizing
# All operations not defined elsewhere are to be placed here

import subprocess
import sys


# TODO: add function description
def read_backup_directory(env: dict):
    # TODO: Create the function code
    # Check if the directory already exists on the machine
    # If not, create it in the default location
    return None


# TODO: add function description
def create_new_backup_save(env: dict):
    # TODO: Create the function code
    # Read the currently active save slots
    # List them to the user
    # Ask which they want to save
    # Create a working copy of the selected save
    # Ask for a name for the backup
    # Check if a backup with such a name already exists
    # If yes, append ".old" to it
    # Rename the working copy
    # If possible, add the Kura5 version to it
    # Move the new backup save to storage
    return None


# TODO: add function description
def load_backup_save(env: dict):
    # TODO: Create the function code
    return None


# TODO: add function description
def request_backup_deletion(env):
    sys.stdout.write("\nWARNING: This operation will delete all backup saves "
                     "currently stored in the default directory.")
    sys.stdout.write("\n\n-----------------------------------------")
    sys.stdout.write("\nPlease type in uppercase YES to continue:")
    deleteSaves = str(sys.stdin.readline())
    if deleteSaves == "YES":
        # TODO: write the deletor code
        sys.stderr.write("\nThe deletion code is not ready yet")
        return None
    else:
        sys.stdout.write("\nDeletion aborted. No files were touched.")
    return None


# TODO: add function description
def open_file_explorer(env: dict):
    sys.stdout.write("\nOpening file explorer in a separate window...")
    if env["Platform"] == "Windows":
        subprocess.Popen('explorer', env["Helperdir-path"])
        return None
    if env["Platform"] == "Linux":
        subprocess.Popen('xdg-open', env["Helperdir-path"])
        return None
    if env["Platform"] == "Darwin":
        subprocess.Popen('open', env["Helperdir-path"])
        return None
    else:
        sys.stderr.write("\nUnsupported platform for this operation")
        return None
