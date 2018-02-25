Shortcut
========

Shortcut is a work in progress solution to help with creating desktop and menu shortcuts for files and applications.

It was created by me to solve a simple problem - if you install python packages using pip there is no way of creating a shortcut to the program.

Shortcut does its best to find your app, searching for the usual suspects in the usual places (i.e. those in the PATH).

Status
------

WORK IN PROGRESS - windows, linux and macos support, massively experimental, probably doesnt work.

Install
-------

(for the moment) Clone the repo and run the setup 

Linux ::

    git clone https://github.com/martinohanlon/shortcut
    cd shortcut
    sudo python3 setup.py install

Windows ::

    git clone https://github.com/martinohanlon/shortcut
    cd shortcut
    python setup.py install


MacOS ::

    git clone https://github.com/martinohanlon/shortcut
    cd shortcut
    python3 setup.py install

Usage
-----

The `shortcut` command line application will create desktop and menu shortcuts ::

    usage: shortcut [-h] [--desktop] [--menu] target

    Auto shortcut creator

    positional arguments:
    target      The target executable to create Desktop and Menu shortcuts

    optional arguments:
    -h, --help  show this help message and exit
    --desktop   Only create a desktop shortcut
    --menu      Only create a menu shortcut

To create a shortcut for an application called `my_app` ::

    shortcut my_app

