.. _`Google Suite chapter`:

Google Suite
============

Google provides a whole bunch of tools that can be used for collaborative
work and in particular in the context of some Software Engineering activities.

Google Drive
------------

ubuntu
''''''

There is no official google drive client for Linux, but you can still
use an open source tool named ``grive`` or much better ``grive2``.

To install ``grive2`` on Ubbunto 14.04::

    sudo add-apt-repository ppa:nilarimogard/webupd8
    sudo apt-get update
    sudo apt-get install grive

Then create a directory (e.g. ``~/GOOGLE_DRIVE``) and initialize
the connection with Google Drive::

    mkdir -p ~/GOOGLE_DRIVE
    cd ~/GOOGLE_DRIVE
    grive -a

By contrast to other clients on other operating system, sychronization
is not run in background and all the time. You have on the contrary to
launch the scynchronization manually::

    grive

Google Document
---------------

Google Spreadsheet
------------------