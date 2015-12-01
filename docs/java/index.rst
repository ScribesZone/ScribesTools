.. _`Java chapter`:

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

On Windows:

    *   Download the jdk from the `java download page`_.
    *   Create the following directory structure::

            %SCRIBESTOOLS%
                Java
                    jre
                    jdk

    *   Install the JDK in ``%SCRIBESTOOLS%\Java\JDK`` and the JRE in
        ``%SCRIBESTOOLS%\Java\jdk``


    *   Add the following directory to the system PATH::

            %SCRIBESTOOLS%\Java\jdk\bin

    *   Set the ``JAVA_HOME`` environment variable to::

            %SCRIBESTOOLS%\Java\jdk

On Ubuntu::

    # Remove existing OpenJDK
    sudo apt-get purge openjdk*
    # Install Oracle Java 8
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer
    # Set Java Environment Variable
    sudo apt-get install oracle-java8-set-default

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

