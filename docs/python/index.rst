Python
======

According to wikipedia "`Python`_ is a widely used general-purpose, high-level
programming language. Its design philosophy emphasizes code readability, and
its syntax allows programmers to express concepts in fewer lines of code than
would be possible in languages such as C++ or Java."

Installation
------------

This section shows how to install Python 2.7.10, how to use create
virtual environments, how to install necessary libraries including windows
specific libraries.

Installing Python 2.7.10
^^^^^^^^^^^^^^^^^^^^^^^^

Detailed information is available in the `BeginnersGuide`_ of python wiki.

.. note::
    There are two python ecosystems: python 2.X and 3.X.
    There some (slight) `language differences`_ between Python 2 and
    Python 3. Since not all libraries have been ported to 3.X Python 2
    is still the most common choice when a lot of libraries are required.


* `Download Python 2.7.10`_. **WARNING: On windows you must select the 32
  bits version** |Python2710Windows32|.

* Install python in a directory like ``C:\S\Python27``. Keep the version
  number (at least 2.7) since it is common to have another directory
  like ``C:\S\Python34`` for Python 3.4.

    msiexec /i  c:\DOWNLOADS\Win\python-2.7.10.msi TARGETDIR=C:\S\Python27
    ALLUSER=1 ADDLOCAL=ALL

* Change the two following directories to the PATH environment variable
  (if not already done by the installation program). ::

    # replace ';' separator by ':' on unix
    # add   C:\S\Python2.7;C:\S\Python2.7\Scripts   to PATH

* To test your installation, open a shell windows and type ``python``.
  The python interpreter should open and you should be able to type
  ``print 'hello world'`` for instance. ``quit()`` will close the interpreter.

Virtual environments
^^^^^^^^^^^^^^^^^^^^
Install `virtualenvwrapper`_ (or `virtualenvwrapper-win`_ on windows).
This can be done with one command (according to your platform)::

    pip install virtualenvwrapper-win   # on windows
    pip install virtualenvwrapper       # otherwise

Create a directory that will contains all virtual environments. For instance
``C:\S\PyVEnvs27``::

    mkdir C:\S\PyVEnvs27

Set the ``WORKON_HOME`` environment variable to the directory just created and
don't forget to open a new shell to see the effects of this change.::

    # define WORKON_HOME variable as C:\S\PyVEnvs27

Use a new shell to create a new virtual environment named `ScribeEnv`::

    mkvirtualenv ScribeEnv
    # this creates a directory ``C:\S\PyVEnvs27\ScribeEnv``.
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

Windows specific libs
^^^^^^^^^^^^^^^^^^^^^
This section is devoted to Windows specific python packages.

.. Note::
    Some python libraries need to be compiled with a C compiler.
    This is tricky on standard windows boxes. When a python library is
    not available for windows, a good idea is to look on the following
    web site:
    `Unofficial Windows Binaries for Python Extension Packages`_.

pywin32
"""""""

pywin32_ is a set of python extensions for Windows. This library is required
in particular by Scrapy_.

* download the 32 bits version ``pywin32-219.win32-py2.7.exe`` |PyWin32|.
* **do not click on the executable** but type instead the following command
  (make sure that ``(ScribeEnv)`` is in the prompt)::

        easy_install C:\DOWNLOADS\pywin32-219.win32-py2.7.exe

pygraphviz
""""""""""
pygraphviz_ is a python API to use the GraphViz_ graph package.

* download ``pygraphviz‑1.3rc2‑cp27‑none‑win32.whl`` |PyGraphViz|. This
  version works with ``graphviz 2.38.msi``.
* **do not click on the executable** but type instead the following command
  (make sure that ``(ScribeEnv)`` is in the prompt)::

        pip install c:\DOWNLOADS\pygraphviz-1.3rc2-cp27-none-win32.whl

pycrypto
""""""""

PyCrypto is a Python cryptography package used by other packages.

* download ``pygraphviz‑1.3rc2‑cp27‑none‑win32.whl`` |PyCrypto|. This
  version works with ``graphviz 2.38.msi``.
* **do not click on the executable** but type instead the following command
  (make sure that ``(ScribeEnv)`` is in the prompt)::

        easy_install.exe c:\DOWNLOADS\pycrypto-2.6.win32-py2.7.exe

Libraries
^^^^^^^^^

::

    # with preliminary downloads
    # pip install --download C:\DOWNLOADS -r requirements.txt
    pip install --no-index --find-links=C:\DOWNLOADS -r requirements.txt

    # both download and install
    pip install XXXX\requirements.txt














Launching Python
----------------

.. ...........................................................................

.. _Python:
    https://www.python.org

.. _`Download Python 2.7.10`:
    https://www.python.org/downloads/release/python-2710/

.. |Python2710Windows32| replace::
    (:download:`local <../../res/python/downloads/Win/python-2.7.10.msi>`,
    `web <https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi>`__)

.. _`BeginnersGuide`:
    https://wiki.python.org/moin/BeginnersGuide

.. _`language differences`:
    https://wiki.python.org/moin/Python2orPython3

.. _`Unofficial Windows Binaries for Python Extension Packages`:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/

.. _`virtualenvwrapper`:
    http://virtualenvwrapper.readthedocs.org/

.. _`virtualenvwrapper-win`:
    https://pypi.python.org/pypi/virtualenvwrapper-win


.. |PyWin32| replace::
    (:download:`local <../../res/python/downloads/Win/pywin32-219.win32-py2.7.exe>`,
    `web <http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe>`__)

.. |PyGraphViz| replace::
    (:download:`local <../../res/python/downloads/Win/pygraphviz-1.3rc2-cp27-none-win32.whl>`,
    `web <http://www.lfd.uci.edu/~gohlke/pythonlibs/3i673h27/pygraphviz-1.3rc2-cp27-none-win32.whl>`__)

.. |PyCrypto| replace::
    (:download:`local <../../res/python/downloads/Win/pycrypto-2.6.win32-py2.7.exe>`,
    `web <http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win32-py2.7.exe>`__)

.. _Scrapy:
    http://scrapy.org/

.. _GraphViz:
    http://graphviz.org/

