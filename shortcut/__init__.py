# get operating system
import sys
platform = sys.platform
if sys.platform.startswith("linux"):
    platform = "linux"

# operating system specific imports
if platform == "win32":
    from .windows import create_shortcut
elif platform == "linux":
    raise Exception("Error: linux not support (coming soon)")
elif platform == "darwin":
    raise Exception("Error: macos not support (coming soon)")
else:
    raise Exception("Error: '{}' platform is not supported.")

def main():
    
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Auto shortcut creator")
    parser.add_argument("target", help="The target app or file to create a shortcut for")
    parser.add_argument("--nodesktop", help="Dont create a desktop shortcut", action="store_true")
    parser.add_argument("--nomenu", help="Dont create a menu shortcut", action="store_true")
    args = parser.parse_args()

    print(args)

    create_shortcut(args.target, not args.nodesktop, not args.nomenu)