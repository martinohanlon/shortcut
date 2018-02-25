Build
=====

Instructions for developing and building shortcut.

Windows
-------

Develop
~~~~~~~

Installing tools::

    pip install pip --upgrade
    pip install setuptools wheel twine

Get repo and install for dev::

    git clone https://github.com/martinohanlon/shortcut
    cd shortcut
    git checkout dev
    python setup.py develop

Deploy
~~~~~~

Create :file:`.pypirc` credentials file::

    notepad %HOMEPATH%\.pypirc

    [distutils]
    index-servers =
        pypi

    [pypi]
    username:
    password:

Build for deployment::

    python setup.py sdist
    python setup.py bdist_wheel

Deploy to `PyPI`_::

    twine upload dist/* --skip-existing

Linux
-------

Develop
~~~~~~~

Installing tools::

    sudo pip3 install pip --upgrade
    sudo pip3 install setuptools wheel twine

Get repo and install for dev::

    git clone https://github.com/martinohanlon/shortcut
    cd shortcut
    git checkout dev
    sudo python3 setup.py develop

Deploy
~~~~~~

Create :file:`.pypirc` credentials file::

    nano ~/.pypirc

    [distutils]
    index-servers =
        pypi

    [pypi]
    username:
    password:

Build for deployment::

    python3 setup.py sdist
    python3 setup.py bdist_wheel

Deploy to `PyPI`_::

    twine upload dist/* --skip-existing

.. _PyPI: https://pypi.python.org/pypi/shortcut