# get operating system
import sys
platform = sys.platform
if sys.platform.startswith("linux"):
    platform = "linux"

# operating system specific imports
if platform == "win32":
    from .windows import create_shortcut, create_desktop_shortcut, create_menu_shortcut, find_target
elif platform == "linux":
    from .linux import create_shortcut
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
    
    try:
        target_path = find_target(args.target)
        create_desktop_shortcut(target_path)
        create_menu_shortcut(target_path)
        print("Shortcut created for '{}'".format(args.target))
    except ShortcutError as e:
        print("Shortcut failed: {}".format(e))

