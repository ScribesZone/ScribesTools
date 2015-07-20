# coding=utf-8

.. _`ReadTheDocs chapter`:

ReadTheDocs
===========

ReadTheDocs_ is a cloud service for publishing and hosting documentation using
the Sphinx_ documentation generator (see :ref:`Sphinx chapter`). The
documentation your are reading is hosted on readthedocs_.

Features
--------
ReadTheDocs_ provide the following services:
* hosting of documentation of open source projects
* continuous Sphinx_ generation (connected to GitHub)
* management of documentation versioning within the browser
* support for downloading documentation in html, pdf, and e-pub formats
* searchable documentation

Installation
------------

No installation is required as this service is on the cloud.
However you must create an `ReadTheDocs account`_.

.. figure:: media/ReadTheDocsAccount.jpg

Then you need to connect this account with your GitHub account. Once this is
done you can import the projects that have sphinx documentation.

.. todo:: to be completed

Usage
-----

Once the ReadTheDocs and GitHub account are connected, the documentation pushed
on the github repository is automatically compiled and published on the
ReadTheDpcs web site.

It is worth to use the `sphinx rtd theme`_ as it provides an excellent
rendering both on computer screens but also on tablet or smart phones.

.. figure:: media/SphinxRTDTheme.png
    :align: center

    `sphinx rtd theme`_

.. todo:: to continue

Documentation
-------------
The web site is rather easy to use, but if you need documentation for specific
topics you can have a look at `ReadTheDocs documentation`_.

.. ............................................................................


.. _ReadTheDocs: https://readthedocs.org/

.. _`ReadTheDocs account`: https://readthedocs.org/accounts/signup/

.. _`ReadTheDocs documentation`: http://docs.readthedocs.org/en/latest/index.html

.. _`sphinx rtd theme`: http://docs.readthedocs.org/en/latest/theme.html
