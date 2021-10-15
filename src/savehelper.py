#!/usr/bin/env python3
# This file is a part of the "kura5-savehelper" project
import os
import platform
import sys

__version__ = 0.1

# Takes the environment variable
# Returns nothing
# Does not do error handling
def get_current_platform(env:dict):
    env["Platform"] = str(platform.system())
    return None

# Takes no parameters
# Returns nothing
# Aborts program on error
def check_savehelper_directory():
    cwdContents = os.listdir(os.getcwd())
    if "savehelper.d" in cwdContents == False:
        sys.stderr.write("The 'savehelper.d' directory was not found. It must "
                         "located in the same directory as the savehelper "
                         "program.")
        sys.exit(2)
    helperdirContents = os.listdir(os.path.abspath("savehelper.d"))
    if not "savecli.py" in helperdirContents:
        sys.stderr.write("The 'savecli.py' file was not found. It must be "
                         "located inside the 'savehelper.d' directory.")
        sys.exit(2)
    if not "libsavehelper.py" in helperdirContents:
        sys.stderr.write("The 'libsavehelper.py' file was not found. It must be"
                         " located inside the 'savehelper.d' directory.")
        sys.exit(2)
    return None

# Takes the environment variable
# Returns nothing
# Does not do error handling
def get_helper_path(env: dict):
    # Stores the absolute path where savehelper.py is located
    env["Helper-path"] = str(os.path.abspath("savehelper.py"))
    return None

# Takes the environment variable
# Returns nothing
# Abort program on error
def check_if_kura5_directory(env: dict):
    cwdContents = os.listdir(os.getcwd())
    # Locate the Kura5 executable
        # "Kura5.x86_64" for Linux
    if env["Platform"] == "Linux":
        if not "Kura5.x86_64" in cwdContents:
            sys.stderr.write("The current directory was not detected as a valid"
                             "Kura5 directory.")
            sys.exit(3)
    if env["Platform"] == "Windows":
        if not "Kura5.exe" in cwdContents:
            sys.stderr.write("The current directory was not detected as a valid"
                             "Kura5 directory.")
            sys.exit(3)
    if not "Kura5_Data" in cwdContents:
        sys.stderr.write("The current directory was not detected as a valid"
                         "Kura5 directory.")
        sys.exit(3)
    return None

# Takes the environment variable
# Returns nothing
# Only warns, does not abort
def get_kura5_version(env: dict):
    gamePath = env["Helper-path"]
    versionInfo = gamePath.split('_')
    if not "ver" in versionInfo[-1]:
        env["Game-version"] = "Unknown"
        return None
    # Continue here

def prepare_for_import(env: dict):
    # Add the "savehelper.d" directory to system path

def main():
    env = {}
    get_current_platform(env)
    check_savehelper_directory()
    get_helper_path(env)
    check_if_kura5_directory(env)
    get_kura5_version(env)
    prepare_for_import(env)
    try:
        import savecli as cli
    except ModuleNotFoundError:
        sys.stderr.write("Could not import the savecli module")
        sys.exit(2)
    #cli.savecli(env)
    sys.exit(0)

main()
