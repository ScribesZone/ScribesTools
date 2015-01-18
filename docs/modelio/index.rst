Modelio
=======

Modelio_ is an open source modeling environment supporting a wide range of
modeling languages: UML_ and BPMN_ in a native form but also SysML_ or TOGAF_
for example.

.. figure:: media/various-models.jpg

Modelio_ is high extensible via `java modules`_,
`python scripts`_ or `python plugins`_. Modelio_ runs on Windows, Mac, and
Linux.

Features
--------

Modelio if a full-fledged modeling environment supporting:

* model edition and validation for a wide range of modeling languages,
* model distribution over the web,
* model versioning with SVN (commercial edition only),
* documentation generation,
* code generation and or reverse engineering of C++, Java, C#, Hibernate, SQL, XSD...

Modelio can be extended to add more features via `java modules`_,
`python scripts`_ or `python plugins`_

Installation
------------

Modelio_ exists both in an open source and commercial version.

.. attention::
    You need either a *node-locked licence* or a *floating licence* to execute
    a commercial version:

    * *node-locked licence* (personal use).
        You may have received a licence code that looks
        like ``3BA5A-AVAT9-RUEJD-WK4LP``. In this case after
        the installation you will have to enter this licence code following
        this procedure |modelio-licence-node|. Beware: a licence code can be used
        only in a single machine and when used on a machine it is *impossible*
        to move to another machine.

    * *floating licence* (with organizations).
        If you are running modelio for the first time in the context of an
        organization (e.g. at UFRIMAG_), Modelio_ may ask you
        to enter the reference of a *licence server* following this procedure
        |modelio-licence-client|. You will have to enter the information of
        the licence server (e.g. at the UFRIMAG_ the host name is
        ``im2ag-ad.e-im2ag.ujf-grenoble.fr`` and the port is ``6200``

.. tip::
    If you have a licence code you can install both an open source version
    and a commercial version on the same machine.

The open source and commercial version(s) of Modelio_ are downloadable at
different places:

* download modelio open source:
    Go to modelio.org download space |modelio-free-download| and select
    the installer for your platform. No registration is required.

* download modelio commercial (*ultimate solution*):
    You will need to:

    #. Register to modelio community |modelio-register|. This is free.
       This will allow you to download commercial products but also to
       participate in modelio forums, etc.
    #. Go to model the *ultimate solution* download space |modelio-ultimate| and
       select the installer for your platform.



Launching Modelio
-----------------
If a shortcut has been created to launch Modelio_ (it depends on your platform),
you just have to click on it. Otherwise you can click on the executable in the
installation directory.

Modelio can be launched within a script or from a shell with a command line
like that (here the installation directory is ``C:\S\Modelio3.2Open\``::

    C:\S\Modelio3.2Open\modelio.exe

It could be wise to create a command to add parameters (or to change the
shortcut on windows) in order to display the console window and run the Modelio_
in debug mode (this allows to have more messages in the console in case of
modelio errors)::

    C:\S\Modelio3.2Open\modelio.exe -mdebug -consoleLog


Documentation
-------------

Documentation on Modelio_ is available from the ``Help > Help`` menu of Modelio_ as shown below. You will most probably want to use the section ``Modelio Modeler`` if you are just interested in using modelio.

.. figure:: media/help.jpg

Different kind of documentation is also available on the web:

* |modelio-documentation-user|
* |modelio-documentation-developers| (for developing extensions)
* |modelio-documentation-faq|
* a few |modelio-documentation-tutorials| (including some |modelio-videos|)

.. tip::
    The |modelio-forums| provides also a very valuable source of information!
    Use the "Search" tab if you want to search some information about a given
    topic.

    .. figure:: media/forums.jpg

.. ............................................................................

.. |modelio-documentation-user| replace::
    `user documentation <https://www.modelio.org/documentation/user-manuals.html>`__

.. |modelio-documentation-developers| replace::
    `developer documentation <https://www.modelio.org/documentation/developer-api.html>`__

.. |modelio-documentation-faq| replace::
    `FAQ <https://www.modelio.org/documentation/faq-menu.html>`__

.. |modelio-documentation-tutorials| replace::
    `tutorials <https://www.modelio.org/documentation/tutorials.html>`__

.. |modelio-videos| replace::
    `videos <https://www.youtube.com/user/ModelioCommunity>`__

.. |modelio-forums| replace::
    `forums <https://www.youtube.com/user/ModelioCommunity>`__

.. |modelio-free-download| replace::
    (`web <https://www.modelio.org/downloads/download-modelio.html>`__)

.. |modelio-register| replace::
    (`web <http://www.modeliosoft.com/en/purchase/user-registration.html?page=shop.registration>`__)

.. |modelio-ultimate| replace::
    (`web <http://www.modeliosoft.com/en/download/ultimate-solution.html>`__)

.. |modelio-licence-node| replace::
    (`web <http://www.modeliosoft.com/licensing/license-activation.html#automatic_activation>`__)

.. |modelio-licence-client| replace::
    (`web <http://www.modeliosoft.com/licensing/license-activation.html#configure_client>`__)

.. |modelio-documentation| replace::
    (`web <http://www.modeliosoft.com/licensing/license-activation.html#configure_client>`__)

.. _Modelio: https://www.modelio.org/

.. _UML: http://en.wikipedia.org/wiki/Unified_Modeling_Language

.. _BPMN: http://en.wikipedia.org/wiki/Business_Process_Model_and_Notation

.. _SysML: http://en.wikipedia.org/wiki/Systems_Modeling_Language

.. _TOGAF: http://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework

.. _WSDL: http://en.wikipedia.org/wiki/Web_Services_Description_Language

.. _`java modules`: http://www.modeliosoft.com/en/modelio-store/modules.html

.. _`python scripts`: http://www.modeliosoft.com/en/modelio-store/scripts.html

.. _`python plugins`: http://PyModelio.readthedocs.org

.. _UFRIMAG: http://ufrima.imag.fr/
