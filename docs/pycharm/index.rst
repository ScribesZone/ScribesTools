.. _`PyCharm chapter`:

PyCharm
=======

PyCharm_ is an excellent IDE for the Python language.

.. figure:: media/PyCharmSplash.jpg

Overview
--------

Python being a dynamic language, using an IDE is a really good idea. This will
help you find errors at development time rather that at runtime. There are
various IDE for pythons around (see `python IDE comparison`_).

If you are going to write non trival python programs for some time, then
we recommend using PyCharm_. It will save you time. PyCharm_ is usually faster,
simpler and more powerful than PyDev_, the python environment on eclipse. If
you are really a huge fan of eclipse, you might prefer PyDev_ indeed.

Installation
------------
There are two versions:

* An open source version which is quite complete and very useful.
* A commercial version which has support for django, databases, etc.

.. Attention::

    If you are student you can very easily get `PyCharm for students`_.
    You just need to register with the email of your university.
    It's really easy and quite fast.

*   `download PyCharm`_ page and then download the appropriate version (e.g.
    Windows community edition |PyCharmOpenWin|, Windows commercial edition
    |PyCharmCommercialWin|).

*   install the version downloaded in a directory like
    ``%SCRIBESTOOLS%\PyCharmOpen`` or ``%SCRIBESTOOLS%\PyCharmCommercial``.
    This naming schema allows to have both editions installed at the same time.

*   by default your personal configuration of PyCharm goes in a directory
    like ``.PyCharm`` in your home directory, but if you want you can change
    this by editing the file ``bin/idea.properties`` in the installation directory.
    You have to adjust for instance the following two lines::

        idea.config.path=Z:/.PyCharm50/config
        idea.system.path=Z:/.PyCharm50/system

.. _`Launching PyCharm section`:

Launching PyCharm
-----------------
The installer most likely created a shortcut. Click on it to launch PyCharm.
Alternatively you can also find the executable in the bin directory of the
installation or in a standard bin directory (e.g. ``/usr/bin/pycharm``).

Launching PyCharm the first time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When launching pycharm for the first time, you will have no ``.PyCharm50``
in your home directory. This directory contains the global configuration
describing your global preference, your environment, the licencing information,
and so on. PyCharm will therefore ask a few questions.

If you use the commercial version of PyCharm, you have to provide information
for:

* your pycharm/jetbrain account (created before) if you work at home for instance,

* or a pycharm server licence if you work at university for instance. If you
  are in the context of the UGA enter
  ``http://im2ag-licence.e-imag.ujf-grenoble.fr:1111`` for the licence server.


Opening/Creating PyCharm projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Just like eclipse or netbeans, PyCharm is NOT a text **file** editor. So one do not
open a file when launching PyCharm, but on the contrary create a **project**
at a given place; and this project (or other projects) will always be opened and
used in next sessions. A PyCharm project is simply a directory with a ``.idea``
subdirectory. This ``.idea`` subdirectoy is created on the first time and then
managed by PyCharm.

*When launching PyCharm you have to select your "project" directory*,
that is the directory that contains all files you want to work on.
Usually this is the directory that also contains versioning information, so
it is most likely that this project directory will contain both ``.idea`` and
``.git`` subdirectories (if you are using Git).

.. note::

    The normal way to proceed with PyCharm is to open only projects and
    you should therefore have only one ``.idea`` directory at the top level
    of your "project directory".

Documentation
-------------
Documentation is available from the ``help`` menu of the tool.

Configuration
-------------

To configure PyCharm_ use the menu ``File > Settings``::

    Editor
        File Encodings
            UTF8
        Appearance
            Show line numbers
            Show method separators
    Code Style
        General
            right margin (columns)

.. ............................................................................

.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _`python IDE comparison`: http://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#Python
.. _`PyCharm for students`: https://www.jetbrains.com/estore/students/
.. _`download PyCharm`: https://www.jetbrains.com/pycharm/download/
.. _PyDev: http://pydev.org/

.. |PyCharmOpenWin| replace::
    (`web <http://download-cf.jetbrains.com/python/pycharm-community-5.0.1.exe>`__)

.. |PyCharmCommercialWin| replace::
    (`web <http://download.jetbrains.com/python/pycharm-professional-5.0.1.exe>`__)



.. ...... notes .....
        .Pycharm50/options/editor.xml
        <application>
          <component name="EditorSettings">
            <option name="ARE_LINE_NUMBERS_SHOWN" value="true" />
          </component>
        </application>
        .PyCharm50/options/filetypes.xml
        <application>
          <component name="FileTypeManager" version="16">
            <ignoreFiles list="*$py.class;*.hprof;*.orig;*.pyc;*.pyo;*.rbc;*~;.DS_Store;.git;.hg;.svn;CVS;RCS;SCCS;__pycache__;_svn;rcs;vssver.scc;vssver2.scc;" />
            <extensionMap>
              <mapping ext="odp" type="Native" />
              <mapping pattern=".nojekyll" type="PLAIN_TEXT" />
              <mapping ext="csv" type="PLAIN_TEXT" />
              <mapping ext="doctree" type="PLAIN_TEXT" />
              <mapping ext="rel" type="PLAIN_TEXT" />
              <mapping ext="inv" type="PLAIN_TEXT" />
              <mapping ext="rstt" type="ReST" />
              <mapping ext="gan" type="XML" />
            </extensionMap>
          </component>
        </application>
        git.xml
        <application>
          <component name="Git.Application.Settings">
            <option name="myPathToGit" value="/usr/bin/git" />    <-----------
            <option name="SSH_EXECUTABLE" value="IDEA_SSH" />
          </component>
        </application>
        github.xml
        <application>
          <component name="GithubSettings">
            <option name="LOGIN" value="escribis" />
            <option name="AUTH_TYPE" value="BASIC" />
          </component>
        </application>
        ide.general.xml
        <application>
          <component name="Registry">
            <entry key="ide.firstStartup" value="false" />
            <entry key="ide.editor.tabs.open.at.the.end" value="true" />
          </component>
        </application>
        jdk.table.xml        ProjectJdkTable    ---- interpreters and virtual env
        <homePath value="/usr/share/PyVEnvs27/ScribesEnv/bin/python" />
      <roots>
        <classPath>
          <root type="composite">
            <root type="simple" url="file:///usr/share/PyVEnvs27/ScribesEnv/lib/python2.7" />
            <root type="simple" url="file:///usr/share/PyVEnvs27/ScribesEnv/lib/python2.7/lib-dynload" />
        runner.layout.xml   <  ---database stuff