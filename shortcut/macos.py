import os
from .exception import *
from .linux import ShortCutterLinux
from tempfile import NamedTemporaryFile
import subprocess

class ShortCutterMacOS(ShortCutterLinux):
            
    def _get_menu_folder(self):
        return os.path.join('/', 'Applications') 
        
    def create_shortcut_file(self, target_name, target_path, shortcut_folder):
        """
        Creates a MacOS app which opens an executable script via the terminal

        Returns a tuple of (target_name, target_path, shortcut_file_path)
        """
        shortcut_file_path = os.path.join(shortcut_folder, target_name + ".app")

        # create the AppleScript script
        sf = NamedTemporaryFile(mode = "w")
        sf.write('tell application "Terminal"\n')
        sf.write('activate\n')
        sf.write('do script "{}"\n'.format(target_path))
        sf.write('end tell\n')
        sf.flush()

        # compile the script into an application
        result = subprocess.run(["osacompile", "-o", shortcut_file_path, sf.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if len(result.stderr):
            raise ShortcutError("Error occured creating app - {}".format(str(result.stderr)))
        sf.close()

        return (target_name, target_path, shortcut_file_path)
