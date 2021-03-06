.. _`Graphviz chapter`:

Graphviz
========

Graphviz_ is a set of tool to deal visualize graphs. See the gallery_.

.. image:: media/examples.jpg

Installation
------------

*   download the installer for your operating system  the `download page`_.

    On Windows ``graphviz-2.38.msi`` must be used, at least if you
    plan to use the pygraphviz_ windows library for python |GraphVizWin|.

    On Ubuntu Graphviz_ can be installed via::

        apt-get install graphviz libgraphviz-dev pkg-config

*   install the program in a directory like ``%SCRIBESTOOLS%\Graphviz\``
*   add ``%SCRIBESTOOLS%\Graphviz\`` into the PATH environment variable.

Launching Graphviz
------------------
To test your installation type the following command in a new shell. It should
display the version of graphviz. ::

    dot -V

You can try the ``gvedit``, a very simple graphical interface. It is not really
useful though as Graphviz_ is mostly used by other programs. ::

    gvedit

Documentation
-------------
There is a lot of documentation_.

.. .............................................................................

.. _Graphviz:
    http://graphviz.org

.. _gallery:
    http://www.graphviz.org/Gallery.php

.. _`download page`:
    http://www.graphviz.org/Download.php

.. _documentation:
    http://www.graphviz.org/Documentation.php

.. _pygraphviz:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz

.. |GraphVizWin| replace::
    `web <http://www.graphviz.org/pub/graphviz/stable/windows/graphviz-2.38.msi>`__
