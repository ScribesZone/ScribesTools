Bulk Installation
=================


Initial Setup
-------------
Set the following environment variables according to your installation and
operating system. On Unix \ must be replaced by / in path and ; should be
replaced by : in the PATH variable. The following variables are given for
Windows::

    SCRIBETOOLS
        C:\ST
    WORKON_HOME
        %SCRIBETOOLS%\PyVEnvs27
    JAVA_HOME
        %SCRIBETOOLS%\Java\jdk
    PATH
        %SCRIBETOOLS%\Java\jdk\bin;%SCRIBETOOLS%\Python27\;%SCRIBETOOLS%\Python27\Scripts;%SCRIBETOOLS%\CheckStyle;%SCRIBETOOLS%\UseOCL\bin;%SCRIBETOOLS%\Graphviz\bin;%SCRIBETOOLS%\KMADe;%SCRIBETOOLS%\SQLite;%SCRIBETOOLS%\SchemaCrawler;%SCRIBETOOLS%\SchemaSpy;%SCRIBETOOLS%\ModelioCommercial;%SCRIBETOOLS%\ModelioOpen;%SCRIBETOOLS%\PyCharmCommercial\bin;%SCRIBETOOLS%\PyCharmOpen\bin;%SCRIBETOOLS%\GanttProject;%SCRIBETOOLS%\Git\cmd;%SCRIBETOOLS%\Pandoc

Once done, open a shell and check the variables (e.g. echo %SCRIBETOOLS%). If
the variables are set properly you can continue to the next steps.

Python
------
Got to the ``res\python`` directory and execute the scripts for your OS in the
given order.

OS dependent packages
---------------------

*   Open a shell and go to the ``res`` directory.
*   Execute the various scripts in the ``bin`` directory

        * java
        * github
        * graphviz
        * pandoc
        * pydoc
        * pycharm
        * (modelio)

Testing the installation
------------------------

To check the installation::

    checkstyle -v
    ganttproject.bat -help
    git help
    dot -V
    java -version
    kmade
    pandoc -v
    schemacrawler -version
    schemaspy
    sqlite3 -version
    use -h
    python --version
    modelio
    pycharm

