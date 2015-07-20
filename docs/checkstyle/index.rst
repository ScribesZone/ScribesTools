.. _`CheckStyle chapter`:

CheckStyle
==========

Checkstyle_ is a `quality control`_  tool  allowing to check adherence of java
programs to coding standards. `Checkstyle`_ is written in java and runs on
all platforms.

Features
--------
`Checkstyle`_ comes by default with configurations files supporting Sun Code
Conventions and Google Java Style but nearly everything can be configured.
New checks can be written in java classes so nearly all kind of coding
standards can virtually  be implemented with `Checkstyle`_.

Interoperability
----------------

`Checkstyle`_ is already integrated in many different IDE in the form of
plugins for instance. There is a large list of `tools related to Checkstyle`_.


Installation
------------

.. tip;
    CheckStyle is integrated as a plugin in many IDE such as Eclipse
    or Netbeans. Please refer to the documentation of your IDE if you just
    want to use it via this plugin. You can also have a look at the
    the list of `tools related to Checkstyle`_.

On Ubuntu you can install CheckStyle_ has following::

    sudo apt-get install checkstyle

Installing CheckStyle_ as a standalone tool is easy:

*   Create a directory ``%SCRIBETOOLS%\CheckStyle``.
*   Download ``checkstyle-X.Y-all.jar`` |checkstyle-jar|.
*   Copy the jar file *into* ``%SCRIBETOOLS%\CheckStyle\checkstyle-all.jar``
    (remove the version number).
*   Copy the files ``checkstyle.cmd`` and ``checkstyle.sh`` into the directory.
*   Add the ``%SCRIBETOOLS%\CheckStyle`` directory to the path.

.. todo::
    update installation section

Launching CheckStyle
--------------------

You check the installation as following. The option ``-h`` and ``-v`` display
the CheckStyle_ help and version respectively::

    checkstyle -h
    checkstyle -v

If you have a java program at hand (let's say ``MyProg.java``) and you want to
use Sun Code Conventions on it type::

    checkstyle -c /sun_checks.xml MyProg.java

Documentation
-------------

A lot of documentation is available online |checkstyle-doc|.

.. ...........................................................................


.. |checkstyle-jar| replace::
    (:download:`local<../../res/checkstyle/downloads/checkstyle-6.8.1-all.jar>`,
    `web <http://sourceforge.net/projects/checkstyle/files/checkstyle/6.8.1/checkstyle-6.8.1-all.jar/>`__)

.. |checkstyle-doc| replace::
    (`web <http://checkstyle.sourceforge.net/index.html>`__)

.. _`CheckStyle`:
    http://checkstyle.sourceforge.net/

.. _`tools related to Checkstyle`:
    http://checkstyle.sourceforge.net/#Related_Tools

.. _`quality control`:
    http://en.wikipedia.org/wiki/Quality_control
