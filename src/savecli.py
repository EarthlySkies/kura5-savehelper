# A part of the "kura5-savehelper" project found on GitHub
# This file contains the user interface definitions and functions
# It also acts as the manager for available operations

import libsavehelper as lib
import sys

__version__ = 0.1


# Returns nothing
# Does not do error handling
def printcli():
    sys.stdout.write("\nThe following operations are available:\n")
    sys.stdout.write("1 - Create a backup copy of currently active save\n")
    sys.stdout.write("2 - Load a backed up save into a save slot\n")
    sys.stdout.write("3 - Open the backup directory in file explorer\n")
    sys.stdout.write("4 - Delete all backed up saves from the system\n")
    sys.stdout.write("0 - Exit\n")
    return None


# Returns nothing
# Does no direct error handling
def operation_selector(env: dict, operation: str):
    if operation == "0":
        sys.exit(0)
    if operation == "1":
        lib.create_new_backup_save(env)
        return None
    if operation == "2":
        lib.load_backup_save(env)
        return None
    if operation == "3":
        lib.open_file_explorer(env)
        return None
    if operation == "4":
        lib.request_backup_deletion(env)
        return None
    else:
        sys.stderr.write("\nInvalid operation requested")
        return None


# Returns nothing
# Handles KeyboardInterrupts
def startcli(env: dict):
    sys.stdout.write("Kura5 Savehelper v. " + str(__version__) + "\n")
    sys.stdout.write("Kura5 version: " + str(env["Game-version"]))
    lib.read_backup_directory(env)
    while True:
        printcli()
        sys.stdout.write("Please input your selected operation: ")
        try:
            selectedOperation = sys.stdin.readline()
        except KeyboardInterrupt:
            sys.exit(0)
        operation_selector(env, selectedOperation)
        continue
