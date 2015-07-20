# coding=utf-8

.. _`Django chapter`:

Django
======

Django_ is a open source web application framework written in Python.
Django's primary goal is to ease the creation of complex, database-driven
websites.

Features
--------
`Django at Glance`_ gives an idea about django development.

Installation
------------

Django is based on python. Follow the instructions in the
:ref:`Python Installation` section if not already done. These instructions
install python but also Django_ as well as many useful Django_ components.

.. Note::

    The installation is done in the ``ScribeEnv`` virtual environment.
    Make sure to execute the following command::

        workon ScribeEnv

    The shell prompt should then start with ``(ScribeEnv)`` meaning that
    you are working in the proper virtual environment.


Launching Django
----------------

If you want to check that Django_ is installed you can try the following::

    workon ScribeEnv
    python -c "import django; print(django.get_version())"
    django-admin --version


Documentation
-------------

In the open source community Django_ is reknown for the quality of its
documentation_. After reading `Django at Glance`_ the best way to start is
to read the `Django Tutorial`_.


.. .............................................................................


..  _`Django`:
    https://www.djangoproject.com/

..  _`documentation`:
    https://docs.djangoproject.com

..  _`Django at Glance`:
    https://docs.djangoproject.com/en/1.8/intro/overview/

..  _`Django Tutorial`:
    https://www.djangoproject.com/

