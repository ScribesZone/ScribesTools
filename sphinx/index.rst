.. _`Sphinx chapter`:

Sphinx
======

Sphinx_ is a documentation generator based on the reStructuredText (rst for
short) for short. It can be used to publish documentation on ReadTheDocs_ (see
:ref:`ReadTheDocs chapter`).

Installation
------------
Sphinx_ is written in Python. Follow the instructions in the
:ref:`Python Installation` section. This will install Python as well as Sphinx_
and related components.

.. Note::

    The installation is done in the ``ScribeEnv`` virtual environment.
    Make sure to execute the following command::

        workon ScribeEnv

    The shell prompt should then start with ``(ScribeEnv)`` meaning that
    you are working in the proper virtual environment.

Launching Sphinx
----------------

To try the installation of Sphinx_ type the following command and press Ctrl-C
to exit from the program::

    sphinx-quickstart

Documentation
-------------

An extensive documentation is available on the Sphinx_ and rst_ web sites. To
learn rst_ different kind of resources are probably better:

*   **Examples**.
    The best way to learn rst_ is probably to look at the source of
    existing rst texts. For instance on ReadTheDocs_ the documentation
    usually include a link ``View Code``.

*   **Cheat Sheets**
    Here is a list of cheat sheets ordered approximatively by size.

        * `CheatSheet #1`_
        * `CheatSheet #2`_
        * `CheatSheet #3`_
        * `CheatSheet #4`_

If you have already some knowledge about markdown you may be interested by
`Markdown vs. rst`_ comparison.

.. todo:: add references to the cheat sheets in docs/



Extensions
----------

* sphinx-contrib_
* `awesome-sphinx`_
* `sphinxext-survey`_

..  _`sphinx-contrib`: https://bitbucket.org/birkenfeld/sphinx-contrib

..  _`sphinxext-survey`: http://sphinxext-survey.readthedocs.org

..  _`awesome-sphinx`: https://github.com/yoloseem/awesome-sphinxdoc

sphinx-googlemaps
^^^^^^^^^^^^^^^^^

:pip: sphinxcontrib-googlemaps

sphinx-googlemaps_ allows to embed maps using Google Maps.

..  _sphinx-googlemaps: https://pypi.python.org/pypi/sphinxcontrib-googlemaps

sphinx-googlechart
^^^^^^^^^^^^^^^^^^

:pip: sphinxcontrib-googlechart

sphinx-googlechart_ allows to embed googlecharts.

..  _sphinx-googlechart: https://pythonhosted.org/sphinxcontrib-googlechart/

sphinx-libreoffice
^^^^^^^^^^^^^^^^^^

:pip: sphinxcontrib-libreoffice

sphinx-libreoffice_ allows to embed libreoffice images.

..  _sphinx-libreoffice: http://pythonhosted.org/sphinxcontrib-libreoffice/

images
^^^^^^

:pip: sphinxcontrib-images


images_ enables thumbnails, fancybox, group of images, captions, tooltip.

..  _images: http://pythonhosted.org/sphinxcontrib-images

css3image
^^^^^^^^^

:pip: sphinxcontrib-css3image

css3image_ provides an enhanced image directive with additional CSS
properties.

..  _css3image: https://github.com/FabriceSalvaire/sphinx-css3image

svg
^^^

:pip: download

svg_ provides svg templates. The name of the extensions is docutils_ext...

..  _svg: https://pypi.python.org/pypi/docutils_ext

swf
^^^

:pip: sphinxcontrib-swf

swf_ allows embedding of flash swf files.

..  _swf: https://bitbucket.org/birkenfeld/sphinx-contrib/src/d27c59cbb3cb986baaba2c312499c2852ccd3f9c/swf

youtube
^^^^^^^

:pip: sphinxcontrib.youtube

youtube_ allows embedding of youtube videos.

..  _youtube: https://pypi.python.org/pypi/sphinxcontrib.youtube

sphinx-embedly
^^^^^^^^^^^^^^

:pip: sphinxcontrib-embedly

sphinx-embedly_ allows to embed whatever can be embedded with embdely_.

..  _sphinx-embedly: https://pypi.python.org/pypi/sphinxcontrib-embedly

..  _embdely: http://embed.ly/


sphinx-twitter
^^^^^^^^^^^^^^

:pip: sphinxcontrib.twitter

sphinx-twitter_ allows to embed tweets.

..  _sphinx-twitter: https://pypi.python.org/pypi/sphinxcontrib.twitter


sphinx-sadisplay
^^^^^^^^^^^^^^^^

:pip: sphinxcontrib-sadisplay

sphinx-sadisplay_ renders SqlALchemy models with PlantUML diagrams or GraphViz directed graphs.

..  _sphinx-sadisplay: https://bitbucket.org/birkenfeld/sphinx-contrib/src/d27c59cbb3cb986baaba2c312499c2852ccd3f9c/sadisplay/

..  _sadisplay: https://bitbucket.org/estin/sadisplay/wiki/Home


schema2rst
^^^^^^^^^^

:pip: schema2rst

schema2rst_ generates reST doc from database schema. Works with
mysql, mysql+pymysql, postgresql.

..  _schema2rst: https://pypi.python.org/pypi/schema2rst

sqltable
^^^^^^^^

:pip: sphinxcontrib-sqltable

sqltable_ allows to embed SQL statements in source documents and produce
tabular output.


..  _sqltable: https://bitbucket.org/dhellmann/sphinxcontrib-sqltable/src

exceltable
^^^^^^^^^^

:pip: sphinxcontrib-exceltable

Exceltable_ adds support for including spreadsheets,
or part of them, into Sphinx document

..  _Exceltable: https://pythonhosted.org/sphinxcontrib-exceltable/

rusty
^^^^^

:pip: rusty

Rusty_ is a collection of extensions:

:rusty.exceltable: Creates table from selected part of the Excel
:rusty.includesh: Extends the standard include directive by converting the given shell script
:rusty.regxlist: Creates bullet list based on regular expression rule. Similar to rolelist directive.
:rusty.rolelist: Creates the bullet list from all the entries of the selected role, with some additonal ways to custom the output.

..  _Rusty: https://pythonhosted.org/rusty/

doctest
^^^^^^^

:pip: standard

doctest_ allows to add test snippets in the documentation in a natural way.
It works by collecting specially-marked up code blocks and running them as
doctest tests.

Within one document, test code is partitioned in groups,
where each group consists of:
*   zero or more setup code blocks (e.g. importing the module to test)
*   one or more test blocks

..  _doctest: http://www.sphinx-doc.org/en/stable/ext/doctest.html


domaintools
^^^^^^^^^^^

:pip: sphinxcontrib-domaintools

domaintools_ provides a tool for easy sphinx domain creation.

..  _domaintools: https://bitbucket.org/klorenz/sphinxcontrib-domaintools


jinjadomain
^^^^^^^^^^^

:pip: sphinxcontrib.jinjadomain

jinjadomain_ provides a Sphinx domain for describing jinja templates.

..  _jinjadomain: https://pythonhosted.org/sphinxcontrib-jinjadomain/

makedomain
^^^^^^^^^^

:pip: sphinxcontrib-makedomain

makedomain_  provides a GNU Make domain.

..  _makedomain: https://bitbucket.org/klorenz/sphinxcontrib-makedomain

phpautodoc
^^^^^^^^^^

:pip: tk.phpautodoc

phpautodoc_ enables to embed PHPDocs to sphinx document.

See also sphinx-php_ and _phpdomain.

..  _phpautodoc: https://pypi.python.org/pypi/tk.phpautodoc

..  _sphinx-php: https://github.com/fabpot/sphinx-php

..  _phpdomain: https://pypi.python.org/pypi/sphinxcontrib-phpdomain

httpdomain
^^^^^^^^^^

:pip: sphinxcontrib-httpdomain

httpdomain_ provides a Sphinx domain for describing RESTful HTTP APIs.

..  _httpdomain: https://pythonhosted.org/sphinxcontrib-httpdomain/

autojs
^^^^^^

:pip: sphinxcontrib-autojs

autojs_  generates a reference documentation from a JavaScript source file.

..  _autojs: https://github.com/lunant/sphinxcontrib-autojs

autoanysrc
^^^^^^^^^^

:pip: sphinxcontrib-autoanysrc

autoanysrc_ insert reST docs from files to target documentation project without auto
generation definitions and signatures.

..  _autoanysrc: https://pypi.python.org/pypi/sphinxcontrib-autoanysrc


autoprogram
^^^^^^^^^^^

:pip: sphinxcontrib-autoprogram

autoprogram_ provides an automated way to document CLI programs. It scans argparse.ArgumentParser object, and
then expands it into a set of .. program:: and .. option:: directives.

..  _autoprogram: http://pythonhosted.org/sphinxcontrib-autoprogram/

autorun
^^^^^^^

:pip: sphinxcontrib-autorun

autorun_ execute the code from a runblock directive and attach the output of the execution to
the document.

..  _autorun: https://bitbucket.org/birkenfeld/sphinx-contrib/src/4fc353dd95019abf3f2b66bda432400b77a2f36a/autorun/doc/index.rst


programoutput
^^^^^^^^^^^^^

:pip: sphinxcontrib-programoutput

programoutput_ inserts the output of arbitrary commands into documents.

..  _programoutput: https://pypi.python.org/pypi/sphinxcontrib-programoutput

jsoncall
^^^^^^^^

:pip: sphinxcontrib-jsoncall

jsoncall_ adds a simple button to perform test calls
to JSON based apis making also possible to change parameters values through
a set of input fields.

..  _jsoncall: https://pypi.python.org/pypi/sphinxcontrib-jsoncall

jsdemo
^^^^^^

:pip: sphinxcontrib-jsdemo

jsdemo_ is an extension for embedding HTML/Javascript demo snippets.

..  _jsdemo: https://pypi.python.org/pypi/sphinxcontrib-jsdemo


releases
^^^^^^^^

:pip: releases

Releases_ is a Sphinx extension designed to help you keep a source control
friendly, merge friendly changelog file & turn it into useful, human readable
HTML output. The source format (kept in your Sphinx tree as changelog.rst)
is a stream-like timeline that plays well with source control & only
requires one entry per change (even for changes that exist in multiple
release lines)

..  _Releases: http://releases.readthedocs.org


sphinx-github
^^^^^^^^^^^^^

:pip: sphinxcontrib-github

sphinx-github_ shows github repos and pull requests.

..  _sphinx-github: https://pypi.python.org/pypi/sphinxcontrib-github


graphvizinclude
^^^^^^^^^^^^^^^

:pip: qubic.sphinx.graphvizinclude

graphvizinclude_ enables graphviz generation of external dot files.

..  _graphvizinclude: https://pypi.python.org/pypi/qubic.sphinx.graphvizinclude

sphinx-yuml
^^^^^^^^^^^

:pip: sphinxcontrib-yuml

sphinx-yuml_ allows rendering of plots using yUML_ service.

..  _sphinx-yuml: https://github.com/njouanin/sphinxcontrib-yuml

..  _yUML: http://yuml.me/

sphinx-seqdiag
^^^^^^^^^^^^^^

:pip: sphinxcontrib-seqdiag

seqdiag_ allows to embed sequence diagrams generated with seqdiag_.

Error message when installing pillow on ubuntu.

..  _sphinx-seqdiag: http://blockdiag.com/en/seqdiag

..  _seqdiag: http://blockdiag.com/en/seqdiag


sphinx-sdedit
^^^^^^^^^^^^^

:pip: sphinxcontrib-sdedit

sphinx-sdedit_ allows to embed seqence diagrams generated with _sdedit.

..  _sphinx-sdedit: https://bitbucket.org/birkenfeld/sphinx-contrib/src/d27c59cbb3cb986baaba2c312499c2852ccd3f9c/sdedit/

..  _sdedit: http://sdedit.sourceforge.net/download/index.html

sphinx-plantuml
^^^^^^^^^^^^^^^

:pip: sphinxcontrib-plantuml

sphinx-plantuml_ enables to embed plantuml_ diagrams.

..  _sphinx-plantuml: https://pypi.python.org/pypi/sphinxcontrib-plantuml

..  _plantuml: http://plantuml.com/

sphinx-pyreverse
^^^^^^^^^^^^^^^^

:pip: sphinx-pyreverse

sphinx-pyreverse_ generates UML diagrams with pyreverse.

..  _sphinx-pyreverse: https://pypi.python.org/pypi/sphinx-pyreverse


slide
^^^^^

:pip: sphinxcontrib-slide

slide_ enable you to embed your slides on slideshare and other sites.

..  _slide: https://bitbucket.org/birkenfeld/sphinx-contrib/src/d27c59cbb3cb986baaba2c312499c2852ccd3f9c/slide



hieroglyph
^^^^^^^^^^

hieroglyph_ slides

..  _hieroglyph: http://docs.hieroglyph.io

tut
^^^

:pip: tut

Tut_ is a tool that helps you write tutorial style documentation
where sections build on one another, and include code examples along the way.

..  _tut: https://github.com/nyergler/tut


spelling
^^^^^^^^

:pip: sphinxcontrib-spelling

sphinxcontrib-spelling_  is a spelling checker for Sphinx. It uses PyEnchant
to produce a report showing misspelled words.

..  _sphinxcontrib-spelling: http://sphinxcontrib-spelling.readthedocs.org

remoteinclude
^^^^^^^^^^^^^

:pip: download

remoteinclude_ is just like literalinclude but for remote files.

..  _remoteinclude: https://gist.github.com/tk0miya/4130196

hiddencode
^^^^^^^^^^

:pip: download

hiddencode_ adds a directive for a highlighted code-block that may be toggled hidden
and shown in HTML

..  _hiddencode: http://scopatz.github.io/hiddencode/

classy-code
^^^^^^^^^^^

:pip: sphinx-classy-code

classy-code_ provides drop-in replacements for Sphinx’ code-block and
literalinclude directives. In addition to specifying emphasize-lines,
you can specify arbitrary classes to add on a per-line basis.

..  _classy-code: https://pypi.python.org/pypi/sphinx-classy-code

getthecode
^^^^^^^^^^

:pip: sphinxcontrib-getthecode

getthecode_ adds a new directive getthecode which is equivalent to
the literalinclude directive, but adds in front of the code block
an header with the file name and an icon to download the file.

..  _getthecode: https://github.com/FabriceSalvaire/sphinx-getthecode

viewcode
^^^^^^^^

:pip: standard

viewcode_ looks at your Python object descriptions (.. class::, ..
function:: etc.) and tries
find the source files where the objects are contained.
When found, a separate HTML page will be output for each module with
a highlighted version of the source code, and a link will be added
to all object descriptions that leads to the source code of the described
object. A link back from the source to the description will also be
inserted.

..  _viewcode: http://www.sphinx-doc.org/en/stable/ext/viewcode.html

linkcode
^^^^^^^^

:pip: standard

linkcode_ is like viewcode but assumes the source code can be found
somewhere on the Internet.

..  _linkcode: http://www.sphinx-doc.org/en/stable/ext/linkcode.html

paramlinks
^^^^^^^^^^

:pip: sphinx-paramlinks

paramlinks_ allows param links in Sphinx function/method descriptions
to be linkable.

..  _paramlinks: https://pypi.python.org/pypi/sphinx-paramlinks


extlinks
^^^^^^^^

:pip: 

traceables
^^^^^^^^^^

:pip: sphinxcontrib-traceables

traceables_ defines traceable items and relationships between them in
documentation generated by Sphinx. It also offers visualization of the
traceables in various forms, such as relationship graphs.

..  _traceables: http://sphinxcontrib-traceables.readthedocs.org

traceability
^^^^^^^^^^^^

:pip: sphinxcontrib-traceability

traceability_ adds directives and roles that serve to identify and relate portions of Sphinx documents and create
lists and traceability matrices based on them.

..  _traceability: https://github.com/ociu/sphinx-traceability-extension


requirements
^^^^^^^^^^^^

:pip: sphinxcontrib-requirements

requirements_ Allows declaring requirement specs wherever in the documentation (for instance, in docstrings
of UnitTest.test_* methods) and displaying them as a single list.

..  _requirements: https://pypi.python.org/pypi/sphinxcontrib-requirements

gen_node
^^^^^^^^

:pip: sphinxcontrib-gen_node

gen_node_ a generic “todo like” nodes.

..  _gen_node: https://pypi.python.org/pypi/sphinxcontrib-gen_node

.. .............................................................................

..  _Sphinx:
    http://sphinx-doc.org/

.. _ReadTheDocs:
    https://readthedocs.org/

.. _rst:
    http://docutils.sourceforge.net/rst.html

..  _`CheatSheet #1`:
    http://github.com/ralsina/rst-cheatsheet/raw/master/rst-cheatsheet.pdf

..  _`CheatSheet #2`:
    https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst

..  _`CheatSheet #3`:
    http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html

.. _`CheatSheet #4`:
    http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html

.. _`Markdown vs. rst`:
    https://gist.github.com/dupuy/1855764