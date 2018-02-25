Shortcut
========

Shortcut is a cross platform command line application and API for creating shortcuts.

It will accept full paths and application names, shortcut doing its best to find your app, searching for the usual suspects in the usual places (i.e. those in the PATH).

To create shortcuts for ``python``:: 

    shortcut python 

It was created to solve a simple problem - if you install a python package using pip there is no simple way of creating a shortcut to the program it installs.

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

Status
------

Alpha (0.0.1) - tested and works but issues_ maybe experienced and API changes are possible.

It should work with Windows, MacOS and Linux operating systems.

.. _issues: https://github.com/martinohanlon/shortcut/issues