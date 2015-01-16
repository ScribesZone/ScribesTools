USE OCL
=======

"`USE`_ is a system for the specification and validation of Information Systems
based on a subset of the Unified Modeling Language (UML) and the
Object Constraint Language (OCL)."

This open source environment has been developed at the University of Bremen and
is available as a `source forge project`_. All the resources available here
have been developed by USE OCL project members under `GPL v2 licence`_

Installation of USE OCL
-----------------------

To install USE OCL on your machine download and extract the file |use-3.0.6.zip|.

For more convenience add the *bin* sub-directory to your system PATH.
For instance the PATH could look like:

*  ``C:\\use-3.0.6\\bin;...rest of the path...`` on Windows or,
*  ``/home/ahmed/use-3.0.6/bin: ... rest ...`` on a Unix-like machine.

.. NOTE::
    On Windows, you can use a OCL language definition for notepad++.
    This will allow you to use this editor with OCL sources "highlighted".

    To install this file:

    * go to "*Main menu > Language > Define your language... > Import ...*\ "
    * select the file |USE_Notepad_plusplus_User_Defined_Language.xml|.
    * You may have to restart notepad++.

Launching USE OCL
-----------------

Once installed, you can just type ``use -nogui`` in a new shell window.
This launch the USE OCL interpreter in the same window.

.. image:: media/USEOCL-shell.jpg

.. NOTE::   On Windows, if you want to use cygwin, then type ``use.bat -nogui``
            otherwise you may encounter problem with the use script.

If you want you can also have a look at the graphical interface (in this case
just type ``use``).

.. image:: media/USEOCL-gui.jpg


Documentation
-------------

The documentation of the USE OCL system is available in the *docs*
directory of this archive.

.. |use-3.0.6.zip| replace::
   ``use-3.0.6.zip`` (
   `local <../../tools/useocl/install/use-3.0.6.zip>`__,
   `web <http://sourceforge.net/projects/useocl/files/USE/3.0.0/>`__)

.. |USE_Notepad_plusplus_User_Defined_Language.xml| replace::
   ``USE_Notepad_plusplus_User_Defined_Language.xml`` (
   `local <../../tools/useocl/install/Win/USE_Notepad_plusplus_User_Defined_Language.xml>`__,,,,,
   `web <http://sourceforge.net/projects/useocl/files/Misc/>`__)

.. _USE: http://sourceforge.net/projects/useocl/
.. _`source forge project`: http://sourceforge.net/projects/useocl/
.. _`GPL v2 licence`: http://www.gnu.org/licenses/gpl-2.0.html
