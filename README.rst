Shortcut
========

Shortcut is a cross platform command line application and API for creating shortcuts.

Shortcut will do its best to find your app, searching for the usual suspects in the usual places (i.e. those in the PATH), or you can give it a full path.

To create desktop and menu shortcuts for ``python``: 

- Using the app:: 

    shortcut python 

- Using the Python API::

    from shortcut import ShortCutter
    s = ShortCutter()
    s.create_desktop_shortcut("python")
    s.create_menu_shortcut("python")

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