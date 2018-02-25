shortcut app
============

Shortcut's command line application creates desktop and menu shortcuts.

It will search for an application if only a name is given or use a direct file path if given.

Usage
-----

To create desktop and menu shortcuts for the `python` application::

    shortcut python

Options
-------

The ``-h`` or ``--help`` option will display the help::

    shortcut --help

::

    usage: shortcut [-h] [--desktop] [--menu] target

    Auto shortcut creator

    positional arguments:
    target      The target executable to create Desktop and Menu shortcuts

    optional arguments:
    -h, --help  show this help message and exit
    --desktop   Only create a desktop shortcut
    --menu      Only create a menu shortcut

To only create a desktop shortcut::

    shortcut --desktop python

Or just a menu shortcut::

    shortcut --menu python
