Java
====

Installation
------------
One should distinguish two java components:

*   **JRE**: The Java Runtime Environment enables **end-users** to **execute**
    java programs.
*   **JDK**: The Java Development Toolkit allows **developers** to **develop**
    java programs.

The JRE can be installed and used independently from the JDK.
By contrast, the JDK comes usually with a JRE. Here are short instructions to
install the JDK (including the JRE).  More information is available on
the `java installation guide`_:

*   Download the jdk from the `java download page`_.
*   Create the following directory structure::

        %SCRIBETOOLS%
            Java
                jre
                jdk

*   Install the JDK in ``%SCRIBETOOLS%\Java\JDK`` and the JRE in
    ``%SCRIBETOOLS%\Java\jdk``


*   Add the following directory to the system PATH::

        %SCRIBETOOLS%\Java\jdk\bin

*   Set the ``JAVA_HOME`` environment variable to::

        %SCRIBETOOLS%\Java\jdk


Launching Java
--------------
To test the JRE type the following command::

    java -version

To test the JDK type the::

    javac -version

.. .............................................................................

.. _`java download page`:
    http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

.. _`java installation guide`:

