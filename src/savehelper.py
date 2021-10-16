#!/usr/bin/env python3
# This file is a part of the "kura5-savehelper" project found on GitHub

import os
import platform
import sys

__version__ = 0.1


# Returns nothing
# Does not do error handling
def get_current_platform(env: dict):
    env["Platform"] = str(platform.system())
    return None


# Returns nothing
# Aborts the program
def savehelper_directory_error_handler(missingFile):
    if missingFile == "savehelper.d":
        sys.stderr.write("The 'savehelper.d' directory was not found. It must "
                         "located in the same directory as this helper "
                         "program. \n")
        sys.exit(2)
    else:
        sys.stderr.write("The '" + missingFile + "' file was not found. It must"
                         " be located inside the 'savehelper.d' directory. \n")
        sys.exit(2)


# Returns nothing
# Aborts program on error
def check_savehelper_directory():
    cwdContents = os.listdir(os.getcwd())
    if "savehelper.d" not in cwdContents:
        savehelper_directory_error_handler("savehelper.d")
    helperdirContents = os.listdir(os.path.abspath("savehelper.d"))
    if "savecli.py" not in helperdirContents:
        savehelper_directory_error_handler("savecli.py")
    if "libsavehelper.py" not in helperdirContents:
        savehelper_directory_error_handler("libsavehelper.py")
    return None


# Returns nothing
# Does not do error handling
def get_helper_paths(env: dict):
    env["Program-path"] = str(os.path.abspath("savehelper.py"))
    env["Helperdir-path"] = str(os.path.abspath("savehelper.d"))
    return None


# Returns nothing
# Aborts the program
def kura5_directory_error_handler():
    sys.stderr.write("The current directory was not detected as a valid"
                     "Kura5 directory. \n")
    sys.exit(3)


# Returns nothing
# Abort program on error
def check_if_kura5_directory(env: dict):
    cwdContents = os.listdir(os.getcwd())
    # Locate the Kura5 executable
    # "Kura5.x86_64" for Linux
    if env["Platform"] == "Linux":
        if "Kura5.x86_64" not in cwdContents:
            kura5_directory_error_handler()
    if env["Platform"] == "Windows":
        if "Kura5.exe" not in cwdContents:
            kura5_directory_error_handler()
    if "Kura5_Data" not in cwdContents:
        kura5_directory_error_handler()
    return None


# Returns nothing
# Does not do error handling
def get_kura5_version(env: dict):
    gamePath = env["Program-path"]
    versionInfo = gamePath.split('_')
    if "ver" not in versionInfo[-1]:
        env["Game-version"] = "Unknown"
        return None
    gameVersion = versionInfo[-1].lstrip('ver')
    # To allow version comparison later, we need a proper decimal number
    if gameVersion[0] == "0":
        if gameVersion[1] != ".":
            gameVersion = gameVersion[:1] + '.' + gameVersion[1:]
    env["Game-version"] = gameVersion
    return None


# Returns nothing
# Does not do error handling
def prepare_for_import(env: dict):
    sys.path.insert(0, str(env["Helperdir-path"]))
    return None


def main():
    env = {}
    get_current_platform(env)
    check_savehelper_directory()
    get_helper_paths(env)
    check_if_kura5_directory(env)
    get_kura5_version(env)
    prepare_for_import(env)
    try:
        import savecli as cli
    except ModuleNotFoundError:
        sys.stderr.write("Could not import the savecli module")
        sys.exit(2)
    cli.startcli(env)
    sys.exit(0)


main()
