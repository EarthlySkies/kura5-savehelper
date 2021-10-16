# A part of the "kura5-savehelper" project found on GitHub
# This is the main library file "savehelper.py" will be utilizing
# All operations not defined elsewhere are to be placed here

import os
import subprocess
import sys


# TODO: add function description
def create_backup_directory(env: dict):
    # TODO: create the function code
    return None


# TODO: add function description
def fetch_backupdir_abspath(env: dict):
    if env["Platform"] == "Windows":
        backupdirAbspath = os.path.abspath("%APPDATA%/LocalLow/Kura5 Devs"
                                           "/Kura5/Savehelper")
        return backupdirAbspath
    if env["Platform"] == "Linux" or "Darwin":
        backupdirAbspath = os.path.expanduser("~/.config/unity3d/Kura5 Devs"
                                              "/Kura5/Savehelper")
        return backupdirAbspath


# TODO: add function description
def does_backupdir_exist(env: dict):
    backupdirPath = fetch_backupdir_abspath(env)
    if not os.path.exists(backupdirPath):
        return False
    return True


# TODO: add function description
def get_backupdir_path(env: dict):
    backupdirPath = fetch_backupdir_abspath(env)
    env["Backupdir-path"] = backupdirPath
    return None


# TODO: add function description
def locate_backup_directory(env: dict):
    if not does_backupdir_exist(env):
        create_backup_directory(env)
    get_backupdir_path(env)
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
    sys.stdout.write("\nWARNING: This operation will delete all currently "
                     "stored backup saves.")
    sys.stdout.write("\n-----------------------------------------")
    sys.stdout.write("\nPlease type in uppercase YES to continue: ")
    deleteSaves = str(sys.stdin.readline()).rstrip('\n')
    if deleteSaves == "YES":
        # TODO: write the deletor code
        sys.stderr.write("\nThe deletion code is not ready yet")
        return None
    else:
        sys.stdout.write("Deletion aborted. No files were touched.")
    return None


# TODO: add function description
def open_file_explorer(env: dict):
    sys.stdout.write("Opening file explorer in a separate window... ")
    if env["Platform"] == "Windows":
        subprocess.Popen(['explorer', env["Backupdir-path"]])
        sys.stdout.write("Done")
        return None
    if env["Platform"] == "Linux":
        subprocess.Popen(['xdg-open', env["Backupdir-path"]])
        sys.stdout.write("Done")
        return None
    if env["Platform"] == "Darwin":
        subprocess.Popen(['open', env["Backupdir-path"]])
        sys.stdout.write("Done")
        return None
    else:
        sys.stderr.write("\nUnsupported platform for this operation")
        return None
