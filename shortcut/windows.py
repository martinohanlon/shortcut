# import win32com
# this often fails due to unable to find DLLs
# so dynamically change the path if required
try:
    import win32com
except ImportError as e:
    if "DLL load failed:" in str(e):
        import os,sys
        path = os.path.join(os.path.split(sys.executable)[0], "Lib","site-packages","pywin32_system32")
        os.environ["PATH"] = os.environ["PATH"] + ";" + path
        try:
            import win32com
        except ImportError as ee:
            dll = os.listdir(path)
            dll = [os.path.join(path,_) for _ in dll if "dll" in _]
            raise ImportError("Failed to import win32com, due to missing DLL:\n" + "\n".join(dll)) from e
    else:
        raise e

import winshell
import sys
import os

def create_shortcut(target, desktop = True, menu = True):
    print(desktop)
    print(menu)
    """
    Creates desktop and menu shortcuts to a target.

    The target can be a fully qualified file path `c:\\Windows\\Notepad.exe`  
    or a simple application name `notepad`.
    """
    # get the target name by removing the extension
    target_name = os.path.splitext(target)[0]
    
    # find for the target path
    target_path = find_target(target)
    print(target_path)

    # create the shortcuts
    if target_path:

        start_folder = winshell.folder("CSIDL_PROGRAMS")
        desktop_folder = winshell.folder("CSIDL_DESKTOPDIRECTORY")

        if desktop:
            winshell.CreateShortcut(
                Path = os.path.join(desktop_folder, target_name + ".lnk"),
                Target = target_path,
                Icon = (target_path, 0),
                Description = "Shortcut to" + target_name)

        if menu:
            winshell.CreateShortcut(
                Path = os.path.join(start_folder, target_name + ".lnk"),
                Target = target_path,
                Icon = (target_path, 0),
                Description = "Shortcut to" + target_name)
    else:
        print("Failed: unable to find '{}'".format(target))

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

    If the target doesn't have an extension, it will search for file which 
    has any of the valid windows executable extensions.

    Directories searched are those in the PATH and it will also attempt
    to search the Python Scripts directory, if that isn't in the PATH.
    """
    # potential list of app paths
    target_paths = []

    # create a list of apps to search for?    
    potential_targets = get_potential_target_names(target)
    
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
                        if file_name.lower() in potential_targets:
                            #print(file_path)
                            target_paths.append(file_path)      
            else:
                # its not a directory, is it the app we are looking for?
                pass

    if len(target_paths) > 0:
        return target_paths[0]
    else:
        return None

def get_potential_target_names(target):
    """
    Gets a list of potential file names which might be the target, by adding
    the windows executable extensions to the target if it doesn't have an
    extension.
    """
    # create a list of potential app names to search for?    
    search_target = []
    
    # does the app have an extension?
    target_ext = os.path.splitext(target)[1]
    if target_ext:
        search_target.append(target.lower())
    else:
        # get windows potential executable extensions
        extensions = os.environ['PATHEXT'].split(os.pathsep)
        for ext in extensions:
            search_target.append((target + ext).lower())

    #print(search_apps)
    return search_target

def get_paths():
    """
    Gets the paths which might contain the target.
    """
    # get folders from PATH
    paths = os.environ['PATH'].split(os.pathsep)
    #print(paths)
    
    # add the python scripts path if needed
    python_scripts_path = get_python_scripts_path()
    #print(python_scripts_path)
    if python_scripts_path:
        found = False
        for path in paths:
            if os.path.exists(path) and os.path.exists(python_scripts_path):
                if os.path.samefile(path, python_scripts_path):
                    found = True
        if not found:
            paths.append(python_scripts_path)
        
    #print(paths)
    return paths

def get_python_scripts_path():
    """
    Gets the Python Scripts path by examining the location of the 
    sys.executable and working backwards through the directory
    structure. 
    
    Returns `None` if it cant be found.
    """
    python_exe_path = sys.executable
    python_path = os.path.dirname(python_exe_path)
    scripts_path = None

    current_path = python_path

    searched = False
    while searched == False:
        path_to_test = os.path.join(current_path, "Scripts")
        if os.path.isdir(path_to_test):
            searched = True
            scripts_path = path_to_test
        else:
            current_path = os.path.dirname(current_path)
            # have we reached the top level
            if os.path.splitdrive(current_path)[1] == "":
                searched = True

    return scripts_path

#print(get_python_scripts_path())
#print(find_app("notepad"))
#shortcut("mu")