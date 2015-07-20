.. _`Pandoc chapter`:

Pandoc
======

Pandoc_ is a converter that allows to transform documents across a very
wide range of documentation formats including html, markdown,
reStructuredText, textile, DocBook, LaTeX, MediaWiki, Word docx,
EPUB, etc.

Installation
------------
See the `installation page`_ for detailed information. Install the application
in a directory like ``%SCRIBETOOLS%\Pandoc``.

On Windows:

* download ``pandoc-1.15-windows.msi`` |PandocWin|.

* if you are on a personal PC just click on the executable.
  If the application should be installed on multiple users
  type instead::

        msiexec /i C:\DOWNLOADS\pandoc-1.15-windows.msi ALLUSERS=1 APPLICATIONFOLDER="%SCRIBETOOLS%\Pandoc"

On Ubuntu::

    sudo apt-get install pandoc

Launching Pandoc
----------------

To test your installation type in a new shell::

    pandoc --version


Documentation
-------------

There is a lot of documentation online. The `user guide`_ describes command
lines options.
.. ............................................................................

.. _Pandoc:
    http://pandoc.org/

.. _`installation page`:
    http://pandoc.org/installing.html

.. |PandocWin| replace::
    (:download:`local <../../res/pandoc/downloads/Win/pandoc-1.15-windows.msi>`, `web <https://github.com/jgm/pandoc/releases/download/1.15/pandoc-1.15-windows.msi>`__)

.. _`user guide`:
    http://pandoc.org/README.html
