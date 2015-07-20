.. _`PyLint chapter`:

PyLint
======

PyLint_ is a quality control tool allowing to check adherence of python programs
to coding standards. PyLint_ is written in Python and runs on all platforms.

Installation
------------

..  todo:: change section to reference general python chapter

Installation instructions |pylint-install| depends on the platform used but
basically PyLint_ is installed via python ``pip`` or platform specific package
installers (e.g. ``apt-get`` on debian or ubuntu). With pip just type::

    pip install pylint

.. attention::
    On windows, make sure that the ``Scripts`` directory of your python
    installation is included in the system path (see :ref:`windowsPath`).
    Some other options are discussed `here <http://docs.pylint.org/installation.html#note-for-windows-users>`__

Lauching PyLint
---------------
To try the installation type::

    pylint --version
    pylint --help

Documentation
-------------
The documentation is available on http://docs.pylint.org/

.. ............................................................................

..  _PyLint: http://www.pylint.org/

..  |pylint-install| replace::
    (`web <http://www.pylint.org/#install>`__)


