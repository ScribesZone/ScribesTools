.. _`SQLite chapter`:

SQLite
======

SQLite_ is a file-based SQL database system.

.. _`SQLite-Installation`:

Installation
------------

*   download the "command line shell” for "sqlite3" from
    `SQLite download page`_.
    For Windows download ``sqlite-shell-win32-x86-3081002.zip``
    |SQLiteWin32zip|.
*   create a directory where you want to install sqlite3 (e.g.
    ``%SCRIBETOOLS%\SQLite``)
*   extract the archive (only one file on windows: ``sqlite3.exe``)
*   move the content of the archive to the directory created
*   add ``%SCRIBETOOLS%\SQLite to the path.

On Ubuntu you can install SQLite_ as following::

    sudo apt-get install sqlite3

The following step is optional, but is useful if you intend to use sqlite3
database from java. This is useful for instance if you plan to use
:ref:`SchemaSpy chapter`.

*   download ``sqlite-jdbc-3.8.10.1.jar`` |SQLiteJDBCJar|
*   copy this jar file in the ``sqlite3`` directory created above
    e.g. ``%SCRIBETOOLS%\sqlite3``)
*   rename this file into ``sqlite-jdbc.jar``



Launching SQLite
-----------------
You can test the installation and check the version of sqlite3 with the
following command::

    sqlite3 -version

Then try::

    sqlite3

This should launch the SQLite_ shell. Try the following commands::

    .help
    .schema
    .quit

Since no database has been specified when launching the shell command the
``.schema`` command will not display anything.


Sqlite3 for django
------------------
If you use SQLite_ with django, then you can launch the shell with the
following commands::

    python manage.py dbshell


Documentation
-------------
To get some help about the command line type::

    sqlite -help

If you want some brief help about the shell commands (including SQL) you can
type in the shell::

    .help

More generally, the documentation is available at
https://www.sqlite.org/cli.html




.. .....................................................................

.. _SQLite:
    https://www.sqlite.org/

.. _`SQLite download page`:
    https://www.sqlite.org/download.html

.. |SQLiteWin32zip| replace::
    (:download:`local <../../res/sqlite/downloads/Win/sqlite-shell-win32-x86-3081002.zip>`,
    `web <https://www.sqlite.org/2015/sqlite-shell-win32-x86-3081002.zip>`__)


.. |SQLiteJDBCJar| replace::
    (:download:`local <../../res/sqlite/downloads/sqlite-jdbc-3.8.10.1.jar>`,
    `web <https://bitbucket.org/xerial/sqlite-jdbc/downloads/sqlite-jdbc-3.8.10.1.jar>`__)
