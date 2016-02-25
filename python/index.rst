.. _`Python chapter`:

Python
======

According to wikipedia "`Python`_ is a widely used general-purpose, high-level
programming language. Its design philosophy emphasizes code readability, and
its syntax allows programmers to express concepts in fewer lines of code than
would be possible in languages such as C++ or Java."

.. _`Python Installation`:

Installation
------------

This section shows how to install Python 2.7, how to use create
virtual environments, how to install necessary libraries including windows
specific libraries. If you want to use Jython/Python in the context
of modelio (see :ref:`Modelio chapter`) you do not have anything to install
as Jython 2.7 is embedded into this tool.

Installing Python 2.7
^^^^^^^^^^^^^^^^^^^^^

Detailed information is available in the `BeginnersGuide`_ of python wiki.
On most unix systems python is usually installed so try ``python -V`` on the
command line. If the version is >= 2.7.6 you can skip this step.

.. note::
    There are two python ecosystems: python 2.X and 3.X.
    There some `language differences`_ between Python 2 and
    Python 3. Since not all libraries have been ported to 3.X Python 2
    is still the most common choice when a lot of libraries are required.


*   `Download Python 2.7.10`_. **WARNING: On windows you must select the 32
    bits version** |Python2710Windows32|.

*   Install python in a directory like ``%SCRIBESTOOLS%\Python27``. Keep the version
    number (at least 2.7) since it is common to have another directory
    like ``%SCRIBESTOOLS%\Python34`` for Python 3.4.

        msiexec /i  c:\DOWNLOADS\Win\python-2.7.10.msi TARGETDIR=%SCRIBESTOOLS%\Python27 ALLUSER=1 ADDLOCAL=ALL

*   Change the two following directories to the PATH environment variable
    (if not already done by the installation program). ::

        # replace ';' separator by ':' on unix
        # add   %SCRIBESTOOLS%\Python2.7;%SCRIBESTOOLS%\Python2.7\Scripts   to PATH

*   To test your installation, open a shell windows and type ``python``.
    The python interpreter should open and you should be able to type
    ``print 'hello world'`` for instance. ``quit()`` will close the interpreter.


Virtual environments
^^^^^^^^^^^^^^^^^^^^
Install `virtualenvwrapper`_ (or `virtualenvwrapper-win`_ on windows).
This can be done with one command (according to your platform)::

    pip install virtualenvwrapper-win   # on windows
    pip install virtualenvwrapper       # otherwise

Create a directory that will contains all virtual environments. For instance
``%SCRIBESTOOLS%\PyVEnvs27``::

    mkdir %SCRIBESTOOLS%\PyVEnvs27

Set the ``WORKON_HOME`` environment variable to the directory just created and
don't forget to open a new shell to see the effects of this change.::

    # define WORKON_HOME variable as %SCRIBESTOOLS%\PyVEnvs27

Use a new shell to create a new virtual environment named ``ScribeEnv``::

    mkvirtualenv ScribeEnv
    # this creates a directory ``%SCRIBESTOOLS%\PyVEnvs27\ScribeEnv``.
    # You should also see that the prompt of the shell is now prefixed with
    # (ScribeEnv) like in the following line:
    # (ScribeEnv) C:\Users\jmfavre>

This ``(ScribeEnv)`` indicates that the python virtual environment used in
this shell is ``ScribeEnv``. This is valid only for *this* shell.
If you want to open another shell you will need to **"activate"** this
virtual environment::

    workon ScribeEnv

From now on, you will have to activate the ScribeEnv virtual environment
each time you open a new shell and want to use/install python software.

Libraries
^^^^^^^^^

Some python libraries depends on the OS (those who are using C libraries for
instance). Select the section corresponding on your OS:

* installing `Python libraries on windows`_.
* installing `Python libraries on unix`_.

.. _`Python libraries on windows`:

Libraries on windows
''''''''''''''''''''

This section is devoted to installing python libraries on windows.

Native libraries
""""""""""""""""

.. Note::
    Some python libraries need to be compiled with a C compiler.
    This is tricky on standard windows boxes. When a python library is
    not available for windows, a good idea is to look on the following
    web site:
    `Unofficial Windows Binaries for Python Extension Packages`_.

pywin32
~~~~~~~

pywin32_ is a set of python extensions for Windows. This library is required
in particular by Scrapy_.

* download the 32 bits version ``pywin32-219.win32-py2.7.exe`` |PyWin32|.
* **do not click on the executable** but type instead the following command
  (make sure that ``(ScribeEnv)`` is in the prompt)::

        easy_install C:\DOWNLOADS\pywin32-219.win32-py2.7.exe

pygraphviz
~~~~~~~~~~

pygraphviz_ is a python API to use the GraphViz_ graph package.

* download ``pygraphviz‑1.3rc2‑cp27‑none‑win32.whl`` |PyGraphViz|. This
  version works with ``graphviz 2.38.msi``.
* **do not click on the executable** but type instead the following command
  (make sure that ``(ScribeEnv)`` is in the prompt)::

        pip install c:\DOWNLOADS\pygraphviz-1.3rc2-cp27-none-win32.whl

pycrypto
~~~~~~~~

PyCrypto is a Python cryptography package used by other packages.

* download ``pygraphviz‑1.3rc2‑cp27‑none‑win32.whl`` |PyCrypto|.
* Type instead the following command
  (make sure that ``(ScribeEnv)`` is in the prompt)::

        easy_install.exe c:\DOWNLOADS\pycrypto-2.6.win32-py2.7.exe

pillow
~~~~~~

Pillow, a replacement for PIL, the Python Image Library.

* download ``Pillow-3.1.1-cp27-none-win32.whl`` |Pillow|.
* Type instead the following command
  (make sure that ``(ScribeEnv)`` is in the prompt)::

        easy_install.exe c:\DOWNLOADS\Pillow-3.1.1-cp27-none-win32.whl

Python libraries
""""""""""""""""

To install regular python libraries (those that are based on python only)
type the following command (make sure that ``(ScribeEnv)`` is in the prompt)::

        pip install XXXX\requirements-windows.txt

..  todo:: Provide requirements-windows.txt



.. _`Python libraries on unix`:

Libraries on Unix
'''''''''''''''''

This section is devoted to installing python libraries on unix.

Native libraries
""""""""""""""""
On **Ubuntu 14.04** the following native libraries have to be installed for python
libraries to work properly.

..  tip::
    For other unix systems try first to install the
    python libraries and check on Google what to do
    if you got error messages.

::

    sudo apt-get install autoconf g++ python2.7-dev python-dev
    sudo apt-get build-dep python-imaging                                                    # for Pillow package
    sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev                # for Pillow package
    sudo apt-get install libffi-dev libssl-dev libxml2-dev libxslt1-dev

Python libraries
""""""""""""""""

To install python libraries on unix change the path in the following command
by the path to your virtualenv directory (e.g. ``/usr/share/PyVEnvs27/ScribesEnv``)
and type the command::

    sudo /<path-to-yout-virtual-env>/bin/pip install requirements-unix.txt


Launching Python
----------------

To test your python installation try the following command::

    python -V


.. _`Python Documentation` :

Documentation
-------------

The best way to find information about python is just to ask question such
as "python read file at once" on google. You may also want to have a
look at |JythonInANutshell| and print a cheat sheet :

    * |CheatSheetA|
    * |CheatSheetB|
    * |CheatSheetC|
    * |FrenchCheatSheetD|
    * |RegExCheatSheet|



.. ...........................................................................

.. _Python:
    https://www.python.org

.. _`Download Python 2.7.10`:
    https://www.python.org/downloads/release/python-2710/

.. _`BeginnersGuide`:
    https://wiki.python.org/moin/BeginnersGuide

.. _`language differences`:
    https://wiki.python.org/moin/Python2orPython3

.. _`Unofficial Windows Binaries for Python Extension Packages`:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/

.. _`install python 2.7.9 on ubuntu`:
    http://shiny1210-blog.logdown.com/posts/259363-how-to-install-python-279-on-ubuntu-1404

.. _`virtualenvwrapper`:
    http://virtualenvwrapper.readthedocs.org/

.. _`virtualenvwrapper-win`:
    https://pypi.python.org/pypi/virtualenvwrapper-win

.. _Scrapy:
    http://scrapy.org/

.. _GraphViz:
    http://graphviz.org/

.. _pywin32:
    http://sourceforge.net/projects/pywin32/

.. _pygraphviz:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz

.. |Python2710Windows32| replace::
    (`web <https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi>`__)

.. |PyWin32| replace::
    (`web <http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe>`__)

.. |PyGraphViz| replace::
    (`web <http://www.lfd.uci.edu/~gohlke/pythonlibs/3i673h27/pygraphviz-1.3rc2-cp27-none-win32.whl>`__)

.. |PyCrypto| replace::
    (`web <http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win32-py2.7.exe>`__)

.. |Pillow| replace::
    (`web <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow>`__)

..  |JythonInANutshell| replace::
    :download:`J/Python in a nutshell<docs/JythonInANutshell-3.pdf>`

..  |CheatSheetA| replace::
    :download:`CheatSheetA<docs/python-cheat-sheet-a.pdf>`

..  |CheatSheetB| replace::
    :download:`CheatSheetB<docs/python-cheat-sheet-b.pdf>`

..  |CheatSheetC| replace::
    :download:`CheatSheetC<docs/python-cheat-sheet-c.png>`

..  |FrenchCheatSheetD| replace::
    :download:`FrenchCheatSheetD<docs/python-french-cheat-sheet-d.pdf>`

..  |RegExCheatSheet| replace::
    :download:`RegExCheatSheet<docs/python-regular-expression-cheat-sheet.pdf>`

..  |RequirementsUbuntu| replace::
    :download:`requirements-ubuntu.txt<../../ScribesStore/tools/python/requirements-ubuntu.txt>`


