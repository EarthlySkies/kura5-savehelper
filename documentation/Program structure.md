The aim of this file is to give an overview of the various components of the program.

---

### The initalizer
- Named "savehelper.py"
- The main executable of the project
- Gets the platform the script is running on
- Verifies that the helper directory structure is intact
- Checks if the program is located inside a Kura5 directory
- Attempts to get the Kura5 version number
- Stores all gathered information in the "env" variable
- Executes the CLI when ready

### The CLI/executor
- Named "savecli.py"
- Asks the users what they want to do
- Handles all I/O operations
- Does all the heavy lifting

### The library
- Named "libsavehelper.py"
- Holds all the functions the CLI will be using
- Basically relocate every possible function to here
