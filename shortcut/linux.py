import sys
import os
import stat
from .exception import *

def create_shortcuts(target, desktop = True, menu = True):
    """
    Creates desktop and menu shortcuts to a target.

    The target can be a fully qualified file path `/usr/bin/gedit`  
    or a simple application name `gedit`.
    """
    # get the target name by getting the file name and removing the extension
    target_name = os.path.splitext(os.path.basename(target))[0]
    
    # find for the target path
    target_path = find_target(target)

    if desktop:
        create_desktop_shortcut(target_path)

    if menu:
        create_desktop_shortcut(target_path)

def create_desktop_shortcut(target):
    """
    Creates a desktop shortcut to a target.

    The target can be a fully qualified file path `/usr/bin/gedit`  
    or a simple application name `gedit`.
    """

    # get the target name by getting the file name and removing the extension
    target_name = os.path.splitext(os.path.basename(target))[0]

    # find for the target path  
    target_path = find_target(target)

    desktop_folder = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    if not os.path.isdir(desktop_folder):
        raise ShortcutNoDesktopError("Desktop folder '{}' not found".format(desktop_folder))

    return create_shortcut_file(target_name, target_path, desktop_folder)

def create_menu_shortcut(target):
    """
    Creates a menu shortcut to a target.

    The target can be a fully qualified file path `/usr/bin/gedit`  
    or a simple application name `gedit`.
    """
    # get the target name by getting the file name and removing the extension
    target_name = os.path.splitext(os.path.basename(target))[0]

    # find for the target path  
    target_path = find_target(target)

    menu_folder = os.path.join(os.path.join(os.path.expanduser('~')), '.local', 'share', 'applications')
    if not os.path.isdir(menu_folder):
        raise ShortcutNoMenuError("Menu folder '{}' not found".format(menu_folder))

    return create_shortcut_file(target_name, target_path, menu_folder) 

def create_shortcut_file(target_name, target_path, shortcut_folder):
    shortcut_file_path = os.path.join(shortcut_folder, "launch_" + target_name + ".desktop")
    with open(shortcut_file_path, "w") as shortcut:
        shortcut.write("[Desktop Entry]\n")
        shortcut.write("Name={}\n".format(target_name))
        shortcut.write("Exec={}\n".format(target_path))
        shortcut.write("Terminal=true\n")
        shortcut.write("Type=Application\n")

        # make the launch file executable
        st = os.stat(shortcut_file_path)
        os.chmod(shortcut_file_path, st.st_mode | stat.S_IEXEC)

    return (target_name, target_path, shortcut_file_path)

def find_target(target):
    """
    Finds the target file path.

    Returns `None` if the file cannot be found.
    """
    if os.path.isfile(target):
        return os.path.abspath(target)
    else:
        targets = search_for_target(target)
        if len(targets) > 0:
            return targets[0]
        else:
            raise ShortcutTargetError("Unable to find '{}'".format(target))

def search_for_target(target):
    """
    Searches for a target file.

    Directories searched are those in the PATH.
    """
    # potential list of app paths
    target_paths = []

    # create list of potential directories
    paths = get_paths()

    # loop through each folder
    for path in paths:
        if os.path.exists(path):
            # is it a directory?
            if os.path.isdir(path):
                # get files in directory
                for file_name in os.listdir(path):
                    file_path = os.path.join(path, file_name)
                    if os.path.isfile(file_path):
                        if file_name == target:
                            # is the file executable
                            if os.access(file_path, os.X_OK):
                                target_paths.append(file_path)      
            else:
                # its not a directory, is it the app we are looking for?
                pass

    return target_paths

def get_paths():
    """
    Gets the paths which might contain the target.
    """
    # get folders from PATH
    paths = os.environ['PATH'].split(os.pathsep)
    
    return paths
