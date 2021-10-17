# A part of the "kura5-savehelper" project found on GitHub
# This is the main library file "savehelper.py" will be utilizing
# All operations not defined elsewhere are to be placed here

import os
import subprocess
import sys


# TODO: add function description
# Consider possible merger with fetch_backupdir_abspath
def fetch_kura5devsdir_abspath(env: dict):
    if env["Platform"] == "Windows":
        kura5DevsDir = os.path.expandvars("%userprofile%/AppData/LocalLow/Kura5"
                                          " Devs/Kura5")
        return kura5DevsDir
    if env["Platform"] == "Linux" or "Darwin":
        kura5DevsDir = os.path.expanduser("~/.config/unity3d/Kura5 Devs/Kura5")
        return kura5DevsDir
    return None


# TODO: add function description
def does_kura5devsdir_exist(env: dict):
    kura5DevsDirAbspath = fetch_kura5devsdir_abspath(env)
    if not os.path.exists(kura5DevsDirAbspath):
        sys.stderr.write("\nLaunch Kura5 before using this utility")
        sys.exit(3)
    return None


# TODO: add function description
def fetch_backupdir_abspath(env: dict):
    if env["Platform"] == "Windows":
        backupdirAbspath = os.path.expandvars("%userprofile%/LocalLow/Kura5 Devs"
                                              "/Kura5/Savehelper")
        return backupdirAbspath
    if env["Platform"] == "Linux" or "Darwin":
        backupdirAbspath = os.path.expanduser("~/.config/unity3d/Kura5 Devs"
                                              "/Kura5/Savehelper")
        return backupdirAbspath


# TODO: add function description
def create_backup_directory(env: dict):
    # TODO: create the function code
    pathToCreate = (fetch_backupdir_abspath(env))
    os.mkdir(pathToCreate)
    return None


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
    does_kura5devsdir_exist(env)
    if not does_backupdir_exist(env):
        create_backup_directory(env)
    get_backupdir_path(env)
    return None


# TODO: add function description
def filename_of_saveslot(saveSlot: int):
    # TODO: write more efficient code
    if saveSlot == 1:
        return "save.bok"
    if saveSlot == 2:
        return "save2.bok"
    if saveSlot == 3:
        return "save3.bok"
    if saveSlot == 4:
        return "save4.bok"
    return None


# TODO: add function description
def make_working_copy(saveSlot: int):
    # TODO: add the function code
    saveToCopy = filename_of_saveslot(saveSlot)
    return None


# TODO: add function description
def list_active_save_slots(listToScan: list):
    # TODO: write more efficient code
    activeSaveList = []
    for i in range(0, len(listToScan)):
        if listToScan[i] == "save.bok":
            activeSaveList.append("1")
    for i in range(0, len(listToScan)):
        if listToScan[i] == "save2.bok":
            activeSaveList.append("2")
    for i in range(0, len(listToScan)):
        if listToScan[i] == "save3.bok":
            activeSaveList.append("3")
    for i in range(0, len(listToScan)):
        if listToScan[i] == "save4.bok":
            activeSaveList.append("4")
    if len(activeSaveList) != 0:
        sys.stdout.write("The following save slots were detected as active: ")
        sys.stdout.write(str(activeSaveList))
    return activeSaveList


# TODO: add the function description
def select_save_slot_to_copy(activeSaves: list):
    while True:
        sys.stdout.write("\nPlease select the slot you want to back up: ")
        selectedSlot = str(sys.stdin.readline()).rstrip('\n')
        if selectedSlot in activeSaves:
            return selectedSlot
        else:
            sys.stderr.write("\nNo such active save slot was found")
            continue


# TODO: add function description
def create_new_backup_save(env: dict):
    # TODO: Create the function code
    sys.stdout.write("\nCreating a backup copy of a save...")
    kura5DataContents = os.listdir(env["Gamedatadir-path"])
    activeSaves = list_active_save_slots(kura5DataContents)
    if len(activeSaves) == 0:
        sys.stderr.write("\nNo active saves could be located")
        return None
    saveSlotToCopy = int(select_save_slot_to_copy(activeSaves))
    make_working_copy(saveSlotToCopy)
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
    sys.stderr.write("\nThe loader code is not ready yet")
    return None


# TODO: add function description
def request_backup_deletion(env):
    sys.stdout.write("\nWARNING: This operation will delete ALL currently "
                     "stored backup saves.")
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
