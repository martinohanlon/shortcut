shortcut app
============

The command line application ``shortcut`` creates desktop and menu shortcuts.

``shortcut`` will search for the app or use a full path if given.

Usage
-----

To create desktop and menu shortcuts for the `python` application::

    shortcut python

Options
-------

The ``-h`` or ``--help`` option will display the help::

    shortcut --help

::

    usage: shortcut [-h] [-d] [-m] target

    Auto shortcut creator

    positional arguments:
    target         The target executable to create Desktop and Menu shortcuts

    optional arguments:
    -h, --help     show this help message and exit
    -d, --desktop  Only create a desktop shortcut
    -m, --menu     Only create a menu shortcut
  
To only create a desktop shortcut use ``--desktop``::

    shortcut --desktop python

Or just a menu shortcut using ``--menu``::

    shortcut --menu python
