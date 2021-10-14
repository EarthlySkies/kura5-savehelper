This document contains the guidelines the project should follow in its totality. 
It's aim is to keep the project consistent across time and space.
All contributers are expected to familiarize themselves with these guidelines.
All contributions are also expected to follow these guidelines.

### General guidelines
- The project language is English. As such, all files, issues, discussions and comments are to be in English
- All text and code files are to be encoded in UTF-8 and non-ASCII characters are to be avoided

### Feature guidelines
- All new versions should be backwards compatible and able to load older saves
- The default backup directory should not be changed under any circumstances

### Code style guidelines
- All code should follow the [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- Function names should be self-explanatory
- Don't comment what is being done. Comment why it is being done
- Documentation should be located inside the wiki, not in the comments
- Functions should be no more than 25 lines in length. If it gets longer, split it up
- All input reading should be done via stdin
- All text output should be done via stdout
- Function names are to be written_in_snakecase()
- Variabe names are to be writtenInCamelCase

### Submission guidelines
- Development should mainly take place in the "unstable" branch
- All new non-trivial submissions are expected to open an issue before a pull request
