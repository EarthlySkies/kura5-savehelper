# Kura5-savehelper
This program aims to allow users to avoid the hassle of manual save management for [Kura5](https://chickenhat.itch.io/kura5-bonds-of-the-undying). 
It is written in Python, runs under Python 3 and aims to be cross-platform compatible. 
The project is open-source software, so feel free to use, copy, modify and redistribute it under the license terms.

# IMPORTANT
Due to the upcoming changes of the save file system in the next Kura5 update, the project will halted for a while.
Save files will be suffled around and a system-wide standard location will be utilized. (Confirmed by the Kura5 Team.)
I will make the necessary changes when the next update is around the corner and make a working release.
Until then, I very much doubt I will finish the current version due it's upcoming breakage.

## Installation and usage
1. Download the latest release from the [releases page](https://github.com/EarthlySkies/kura5-savehelper/releases)
2. Extract the contents of the release package
3. Transfer the "savehelper.d" directory to your Kura5 folder 
4. Move the "savehelper.py" out of the "savehelper.d" directory
5. Launch the helper from your file explorer or terminal
6. The program is now running and will ask you what you want to do

---

### About the program

#### Features
- Create backups of your currently active saves
- Load backup saves into any save slot
- Backups are automatically compressed to reduce disk usage

#### Warnings
- After selecting which save slot to insert a backup save into, the helper will overwrite any active save in that slot without warning
- If instructed, the helper can and will delete all backed up saves and remove the backup directory from the system entirely

#### Locations
The backup saves will always be located inside the same directory, regardless of Kura5 version
- On Windows NT -based systems, this will be `%APPDATA%\LocalLow\Kura5 Devs\Kura5\Savehelper`
- On UNIX-based systems, this will be `~/.config/unity3d/Kura5 Devs/Kura5/Savehelper`

#### Linux dependencies
Please verify the package names for your distribution of choise
- `coreutils` for file, directory and permissions management
- `xdg-utils` for file explorer usage
- `python3` for script execution
- `tar` for archived backup saves
- `xz` for backup compression support
- `zip` and `unzip` for importing saves

## Learn more about the project
- Take a deep dive into the documentation in the [wiki](https://github.com/EarthlySkies/kura5-savehelper/wiki)
- Report bugs [here](https://github.com/EarthlySkies/kura5-savehelper/labels/bug), but check 
[this](https://github.com/EarthlySkies/kura5-savehelper/issues/new/choose) first to avoid duplicates
- Suggest features [here](https://github.com/EarthlySkies/kura5-savehelper/labels/enhancement), but check 
[this](https://github.com/EarthlySkies/kura5-savehelper/issues/new/choose) first to avoid duplicates
- See who made this project possible in the  [credits](https://github.com/EarthlySkies/kura5-savehelper/blob/main/AUTHORS.md)
- Worried about vulnerabilities? Check out the [security center](https://github.com/EarthlySkies/kura5-savehelper/security)
