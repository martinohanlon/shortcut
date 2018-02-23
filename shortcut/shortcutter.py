import sys
import os
import stat
from .exception import *

class ShortCutter(object):

    def __init__(self):
        self._desktop_folder = self._get_desktop_folder()
        self._menu_folder = self._get_menu_folder()

    # should be overridden
    def _get_desktop_folder(self):
        raise ShortcutError("_get_desktop_folder needs overriding")
    
    # should be overridden
    def _get_menu_folder(self):
        raise ShortcutError("_get_menu_folder needs overriding")

    def create_desktop_shortcut(self, target):
        """
        Creates a desktop shortcut to a target.

        The target can be a fully qualified file path `/usr/bin/gedit`  
        or a simple application name `gedit`.
        """

        # get the target name by getting the file name and removing the extension
        target_name = os.path.splitext(os.path.basename(target))[0]

        # find for the target path  
        target_path = self.find_target(target)

        if not os.path.isdir(self._desktop_folder):
            raise ShortcutNoDesktopError("Desktop folder '{}' not found".format(self._desktop_folder))

        return self.create_shortcut_file(target_name, target_path, self._desktop_folder)

    def create_menu_shortcut(self, target):
        """
        Creates a menu shortcut to a target.

        The target can be a fully qualified file path `/usr/bin/gedit`  
        or a simple application name `gedit`.

        Returns a tuple of (target_name, target_path, shortcut_file_path)
        """
        # get the target name by getting the file name and removing the extension
        target_name = os.path.splitext(os.path.basename(target))[0]

        # find for the target path  
        target_path = self.find_target(target)

        if not os.path.isdir(self._menu_folder):
            raise ShortcutNoMenuError("Menu folder '{}' not found".format(self._menu_folder))

        return self.create_shortcut_file(target_name, target_path, self._menu_folder) 

    #needs overriding
    def create_shortcut_file(self, target_name, target_path, shortcut_folder):
        raise ShortcutError("create_shortcut_file needs overriding")
        
    def find_target(self, target):
        """
        Returns a target file path.

        Raises ShortcutTargetError if the target cannot be found.
        """
        if os.path.isfile(target):
            return os.path.abspath(target)
        else:
            targets = self.search_for_target(target)
            if len(targets) > 0:
                return targets[0]
            else:
                raise ShortcutTargetError("Unable to find '{}'".format(target))

    def search_for_target(self, target):
        """
        Searches for a target file.

        Returns a list of potential file paths.
        """
        # potential list of app paths
        target_paths = []

        # create list of potential directories
        paths = self.get_paths()

        # loop through each folder
        for path in paths:
            if os.path.exists(path):
                # is it a directory?
                if os.path.isdir(path):
                    # get files in directory
                    for file_name in os.listdir(path):
                        file_path = os.path.join(path, file_name)
                        if os.path.isfile(file_path):
                            if self._is_file_the_target(target, file_name, file_path):
                                target_paths.append(file_path)
                else:
                    # its not a directory, is it the app we are looking for?
                    pass

        return target_paths

    # needs overriding
    def _is_file_the_target(self, target, file_name, file_path):
        raise ShortcutError("_is_file_the_target needs overriding")

    def get_paths(self):
        """
        Gets paths from the PATH environment variables.

        Returns a list of paths.
        """
        # get folders from PATH
        paths = os.environ['PATH'].split(os.pathsep)
        
        return paths
