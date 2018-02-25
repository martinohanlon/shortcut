Operating Systems
=================

Shortcut support Windows, MacOS and Linux.

The way shortcuts are provide and applications launched depends on the operating system.

Windows 
-------

``.lnk`` files pointing directly to the application paths are created in the User Desktop (``CSIDL_DESKTOPDIRECTORY``) and Program (``CSIDL_PROGRAMS``) folders.

MacOS
-----

MacOS applications are created which run the application via a terminal and copied to the User Desktop (``~/Desktop``) and Launchpad (``/Applications``).

Linux
-----

``.desktop`` files are created which start the application via the shell and created in the User Desktop (``~/Desktop``) and applications menu (``~/.local/share/applications``).

