Shortcut
========

Shortcut is a work in progress solution to help with creating desktop and menu shortcuts for files and applications.

It was created by me to solve a simple problem - if you install python packages which have 'executables' using pip there are no way of creating shortcuts.

Shortcut does its best to find your app, searching for the typical subjects in the usual places.

Status
------

WORK IN PROGRESS - windows and linux support, massively experimental, probably doesnt work.

Usage
-----

The `shortcut` command line application will create desktop and menu shortcuts::

usage: shortcut [-h] [--nodesktop] [--nomenu] target

Auto shortcut creator

positional arguments:
  target       The target app or file to create a shortcut for

optional arguments:
  -h, --help   show this help message and exit
  --nodesktop  Dont create a desktop shortcut
  --nomenu     Dont create a menu shortcut


To create a shortcut for an application called `my_app`::

shortcut my_app

