# import win32com
# this often fails due to unable to find DLLs
# so dynamically change the path if required
try:
    import win32com
except ImportError as e:
    if "DLL load failed:" in str(e):
        import os
        import sys
        path = os.path.join(os.path.split(sys.executable)[0], "Lib", "site-packages", "pywin32_system32")
        os.environ["PATH"] = os.environ["PATH"] + ";" + path
        try:
            import win32com
        except ImportError as ee:
            dll = os.listdir(path)
            dll = [os.path.join(path, _) for _ in dll if "dll" in _]
            # TODO: Python version 2.7 does not support this syntax:
            raise ImportError("Failed to import win32com, due to missing DLL:\n" + "\n".join(dll)) from e
    else:
        raise e

import winshell
import sys
import os
from .base import ShortCutter


class ShortCutterWindows(ShortCutter):
    def _custom_init(self):
        self.executable_file_extensions = os.environ['PATHEXT'].split(os.pathsep)

    def _get_desktop_folder(self):
        return winshell.desktop()

    def _get_menu_folder(self):
        return winshell.folder("CSIDL_PROGRAMS")

    def _get_site_packages(self):
        """
        Returns site packages dir path
        (the one to where setup.py installs if use `ShortCutter()` from setup.py).
            Works (tested) only on Miniconda.
        """
        return os.path.join(os.path.dirname(sys.executable), 'Lib', 'site-packages')

    def _get_bin_folder(self):
        """
        Returns `Scripts` dir path
        (the one to where setup.py installs if use `ShortCutter()` from setup.py).
            Works (tested) only on Miniconda.
        """
        return os.path.join(os.path.dirname(sys.executable), "Scripts")

    def _create_shortcut_to_dir(self, shortcut_name, target_path, shortcut_directory):
        return self._create_shortcut_file(shortcut_name, target_path, shortcut_directory)

    def _create_shortcut_file(self, shortcut_name, target_path, shortcut_directory):
        """
        Creates a Windows shortcut file.

        Returns shortcut_file_path
        """
        shortcut_file_path = os.path.join(shortcut_directory, shortcut_name + ".lnk")

        winshell.CreateShortcut(
            Path=shortcut_file_path,
            Target=target_path,
            Icon=(target_path, 0),
            Description="Shortcut to" + os.path.basename(target_path),
            StartIn=target_path)

        return shortcut_file_path

    def _is_file_the_target(self, target, file_name, file_path):
        match = False
        # does the target have an extension?
        target_ext = os.path.splitext(target)[1]
        # if so, do a direct match
        if target_ext:
            if file_name.lower() == target.lower():
                match = True
        # no extension, compare the target to the file_name for each executable file extension
        else:
            for extension in self.executable_file_extensions:
                if file_name.lower() == (target + extension).lower():
                    match = True
        return match

    def _get_paths(self):
        """
        Gets paths from the PATH environment variable and (if possible)
        the path of the Python/Scripts directory.

        Returns a list of paths.
        """
        # noinspection PyProtectedMember
        paths = super(ShortCutterWindows, self)._get_paths()

        # add the python scripts path
        python_scripts_path = self._get_python_scripts_path()
        if python_scripts_path not in paths:
            paths.append(python_scripts_path)

        return paths

    # noinspection PyMethodMayBeStatic
    def _get_python_scripts_path(self):
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
        while not searched:
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
