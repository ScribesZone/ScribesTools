Graphviz
========

Graphviz_ is a set of tool to deal visualize graphs. See the gallery_.

.. image:: media/examples.jpg

Installation
------------

*   go to the `download page`_ and download the page for your operation system.
    ``graphviz-2.38.msi`` must be used on windows if you plan to use the
    pygraphviz_ windows library for python |GraphVizWin|.
*   install the program in a directory like ``C:\S\Graphviz\``

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
    (:download:`local<../../res/graphviz/downloads/Win/graphviz-2.38.msi>`,
    `web <http://www.graphviz.org/pub/graphviz/stable/windows/graphviz-2.38.msi>`__)
