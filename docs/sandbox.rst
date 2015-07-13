(SANDBOX)
=========
This page is just for testing/prototyping documentation features.


.. todo:: check toogle features and add it to hide long section

.. todo:: improve the styling of toogle and support more blocks




Toogle
------

.. _`this post`:
    http://stackoverflow.com/questions/2454577/sphinx-restructuredtext-show-hide-code-snippets

Examples from `this post`_ do not work:

..  container::

    ..  container:: header

        show/hide

    ..  code-block:: xml
        :linenos:

        from plone import api
        ...

another example

..  admonition:: Solution
    :class: toogle

    To save the world with only seconds to spare do the following:

    .. code-block:: python

        from plone import api


The example from the web site work more or less:

..  admonition:: Solution
    :class: toggle

    To save the world with only seconds to spare do the following:

    .. code-block:: python

        from plone import api




Tooltips
--------

Here there is a abbr to get a tooltip. :abbr:`LIFO (last-in,
first-out, ldfjqslkdjf, <br/>dfqskjdf)`. But unfortunately there is no support
for HTML/

Misc
----

And :guilabel:`target`. with a menu :menuselection:`Start --> Programs`

:samp:`print 1+{variable}`

Test [#f1]_ is a footnote? This is antoher [#f2]_ .

This is a var :envvar:PATH with quote :envvar:`PATH`.

A command :command:`ls -ls` and a file:`toto\\titi`



.. [#f1] this is the txt of the footnote

.. [#f2] the second one

