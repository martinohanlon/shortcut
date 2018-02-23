# get operating system
import sys
platform = sys.platform
if sys.platform.startswith("linux"):
    platform = "linux"

# operating system specific imports
if platform == "win32":
    from .windows import ShortCutterWindows as ShortCutter
elif platform == "linux":
    from .linux import  ShortCutterLinux as ShortCutter
elif platform == "darwin":
    raise Exception("Error: macos not support (coming soon)")
else:
    raise Exception("Error: '{}' platform is not supported.")

from .exception import *

def main():
    
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Auto shortcut creator")
    parser.add_argument("target", help="The target app or file to create a shortcut for")
    parser.add_argument("--nodesktop", help="Dont create a desktop shortcut", action="store_true")
    parser.add_argument("--nomenu", help="Dont create a menu shortcut", action="store_true")
    args = parser.parse_args()
    
    print("new shortcutter")
    shortcutter = ShortCutter()

    try:
        target_path = shortcutter.find_target(args.target)

        desktop_created = False
        try:
            print(shortcutter.create_desktop_shortcut(target_path))
            desktop_created = True
        except ShortcutNoDesktopError as e:
            print("Failed to create desktop shortcut")
            print(e)
        
        menu_created = False
        try:
            print(shortcutter.create_menu_shortcut(target_path))
            menu_created = True
        except ShortcutNoMenuError as e:
            print("Failed to create menu shortcut")
            print(e)
        
        if desktop_created or menu_created:
            print("Shortcut created for '{}'".format(args.target))

    except ShortcutError as e:
        print("Shortcut failed: {}".format(e))

