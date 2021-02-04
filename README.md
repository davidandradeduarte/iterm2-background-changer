# iTerm2 Background Changer

This program uses iTerm2 Python API to (randomly) change the image background of your terminal with a simple command.

```bash
    python change_background.py
    python remove_background.py
```

Or if you want to run as executable

```bash
    # Make the file executable with
    chmod +x change_background.py
    chmod +x remove_background.py
    # Execute with
    ./change_background.py
    ./remove_background.py
```

## Arguments

```bash
    python change_background.py path_to_dir
    python change_background.py path_to_file
```

Currently the program only reads the first argument it's given.  
It can be a **specific file** or **folder**.  

**In case it's a folder, the program will choose a random image! That's the fun part 😉**

The default value for the directory is `imgs/`  
*(includes some chill lofi anime wallpapers too)*

## TODOS / Limitations

- Only pick image files. Currently the program will read and pick a random file from the passed directory.
