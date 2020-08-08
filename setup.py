import sys

import cx_Freeze

base = None
if sys.platform == "win32":
    base = "Win32GUI"
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "snakes",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\snakes.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="snakes.py", icon='icon.ico', base=base)]

cx_Freeze.setup(
    version="1.0",
    description="snake game",
    author="Nikhil",
    name="snakes",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ['icon.ico', 'welcome.jpg', 'snake.jpg', 'gameover.jpg', 'hiscore.txt',
                                             'welcome.mp3', 'back.mp3', 'gameover.mp3']},
             "bdist_msi": bdist_msi_options,
             },
    executables=executables

)
