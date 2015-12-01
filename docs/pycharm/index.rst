.. _`PyCharm chapter`:

PyCharm
=======

PyCharm_ is an excellent IDE for the Python language.

.. figure:: media/PyCharmSplash.jpg

Overview
--------

Python being a dynamic language, using an IDE is a really good idea. This will
help you find errors at development time rather that at runtime. There are
various IDE for pythons around (see `python IDE comparison`_).

If you are going to write non trival python programs for some time, then
we recommend using PyCharm_. It will save you time. PyCharm_ is usually faster,
simpler and more powerful than PyDev_, the python environment on eclipse. If
you are really a huge fan of eclipse, you might prefer PyDev_ indeed.

Installation
------------
There are two versions:

* An open source version which is quite complete and very useful.
* A commercial version which has support for django, databases, etc.

.. Attention::

    If you are student you can very easily get `PyCharm for students`_.
    You just need to register with the email of your university.
    It's really easy and quite fast.

*   `download PyCharm`_ page and then download the appropriate version (e.g.
    Windows community edition |PyCharmOpenWin|, Windows commercial edition
    |PyCharmCommercialWin|).

*   install the version downloaded in a directory like
    ``%SCRIBESTOOLS%\PyCharmOpen`` or ``%SCRIBESTOOLS%\PyCharmCommercial``.
    This naming schema allows to have both editions installed at the same time.

*   by default your personal configuration of PyCharm goes in a directory
    like ``.PyCharm40`` in your home directory, but if you want you can change
    this by editing the file ``bin/idea.properties`` in the installation directory.
    You have to adjust for instance the following two lines::

        idea.config.path=Z:/.PyCharm/config
        idea.system.path=Z:/.PyCharm/system


Launching PyCharm
-----------------
The installers most likely created a shortcut. Click on it to launch PyCharm.
Alternatively you can also find the executable in the bin directory of the
installation.

Documentation
-------------
Documentation is available from the ``help`` menu of the tool.

Configuration
-------------

To configure PyCharm_ use the menu ``File > Settings``::

    Editor
        File Encodings
            UTF8
        Appearance
            Show line numbers
            Show method separators
    Code Style
        General
            right margin (columns)

.. ............................................................................

.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _`python IDE comparison`: http://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#Python
.. _`PyCharm for students`: https://www.jetbrains.com/estore/students/
.. _`download PyCharm`: https://www.jetbrains.com/pycharm/download/
.. _PyDev: http://pydev.org/

.. |PyCharmOpenWin| replace::
    (:download:`local <../../res/pycharm/downloads/Win/pycharm-community-4.5.4.exe>`,
    `web <http://download.jetbrains.com/python/pycharm-community-4.5.3.exe>`__)

.. |PyCharmCommercialWin| replace::
    (:download:`local <../../res/pycharm/downloads/Win/pycharm-professional-4.5.4.exe>`,
    `web <http://download.jetbrains.com/python/pycharm-professional-4.5.3.exe>`__)

