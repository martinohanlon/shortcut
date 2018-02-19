import sys
import os
import stat

def create_shortcut(target, desktop = True, menu = True):
    """
    Creates desktop and menu shortcuts to a target.

    The target can be a fully qualified file path `/usr/bin/gedit`  
    or a simple application name `gedit`.
    """
    # get the target name by removing the extension
    target_name = os.path.splitext(target)[0]
    
    # find for the target path
    target_path = find_target(target)

    # create the shortcuts
    if target_path:

        menu_folder = os.path.join(os.path.join(os.path.expanduser('~')), '.local', 'share', 'applications')
        if not os.path.isdir(menu_folder):
            print("Couldn't find the menu folder '{}'".format(menu_folder))
            menu = False
        
        desktop_folder = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        if not os.path.isdir(desktop_folder):
            print("Couldn't find the desktop folder '{}'".format(desktop_folder))
            desktop = False
        
        if desktop:
            write_shortcut_file(desktop_folder, target_name, target_path)

        if menu:
            write_shortcut_file(menu_folder, target_name, target_path)

    else:
        print("Failed: unable to find '{}'".format(target))

def write_shortcut_file(shortcut_folder, target_name, target_path):
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

def find_target(target):
    """
    Finds the target file path.

    Returns `None` if the file cannot be found.
    """
    if os.path.isfile(target):
        return os.path.abspath(target)
    else:
        return search_for_target(target)

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

    if len(target_paths) > 0:
        return target_paths[0]
    else:
        return None

def get_paths():
    """
    Gets the paths which might contain the target.
    """
    # get folders from PATH
    paths = os.environ['PATH'].split(os.pathsep)
    
    return paths
