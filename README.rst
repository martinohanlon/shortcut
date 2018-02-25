Shortcut
========

|pypibadge| |docsbadge|

Shortcut is a cross platform command line application and API for creating shortcuts.

``shortcut`` will do its best to find your app, searching for the usual suspects in the usual places (i.e. those in the PATH), or you can give it a full path.

To create desktop and menu shortcuts for ``python``: 

- Using the app:: 

    shortcut python 

- Using the Python API::

    from shortcut import ShortCutter
    s = ShortCutter()
    s.create_desktop_shortcut("python")
    s.create_menu_shortcut("python")

It was created to solve a simple problem - if you install a python package using ``pip`` there is no simple way of creating a shortcut to the program it installs.

Documentation
-------------

There is comprehensive documentation at `shortcut.readthedocs.io`_.

Install
-------

Shortcut is available on pypi_ and can be installed using ``pip``:

- Windows ::

    pip install shortcut

- MacOS ::

    pip3 install shortcut

- Linux ::

    sudo pip3 install shortcut

Status
------

Alpha - tested and works but issues_ maybe experienced and API changes are possible.

It should work with Windows, MacOS and Linux operating systems.

.. _issues: https://github.com/martinohanlon/shortcut/issues
.. _pypi: https://pypi.python.org/pypi/shortcut
.. _shortcut.readthedocs.io: https://shortcut.readthedocs.io

.. |pypibadge| image:: https://badge.fury.io/py/shortcut.svg
   :target: https://badge.fury.io/py/bluedot
   :alt: Latest Version

.. |docsbadge| image:: https://readthedocs.org/projects/shortcut/badge/
   :target: https://readthedocs.org/projects/shortcut/
   :alt: Docs