#!/usr/bin/env python3

import os
from os import path
import sys
import iterm2
from random import randrange

async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    profile = await session.async_get_profile()

    arg = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if not path.exists(arg):
            print('File or folder not found.')
            return
        if os.path.isfile(arg):
            await profile.async_set_background_image_location(os.path.abspath(arg))
            return

    directory = arg if arg is not None else 'imgs'
    dir = os.fsencode(directory)
    if not path.exists(dir):
        print('File or folder not found.')
        return

    n_files = len(os.listdir(dir))

    if n_files > 0:
        rand_number = randrange(n_files)
        file = os.listdir(dir)[rand_number]
        filename = os.fsdecode(file)

        await profile.async_set_background_image_location(os.path.abspath(f'{directory.rstrip("/")}/{filename}'))

iterm2.run_until_complete(main)
