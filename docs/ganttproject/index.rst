GanttProject
============

`GanttProject`_ is a free `project management`_ tool allowing to edit `gantt models`_ but also view `pert models`_ and `resource allocation models`_. As this tools is written in java it runs on all platforms.

Features
--------

`GanttProject`_ allows to create *milestones* and hierarchies of *tasks*
related with *dependency constraints*. Different *fields* can be attached to
milestones and tasks, for instance "priority", "cost", "start date",
"duration", etc. *Custom fields* can also be added.

.. figure:: media/gantt.png

    *gantt diagram* of the `house building example`_

`GanttProject`_ is mostly an editor for `gantt models`_ editor (as shown
above) but as shown below `pert models`_ can be generated as read-only
views.

.. figure:: media/pert.jpg

    *pert diagram* of the `house building example`_

`GanttProject`_ also supports `resource allocation models`_. *Resources* can be
attached to *tasks* and the tool will generate a resource allocation models showing the allocation of each resource along the project.

.. figure:: media/resource.png

    *resource allocation model* of the `house building example`_

Interoperability
----------------

Microsoft Project and CSV files can be imported and exported. `GanttProject`_
can also generate PDF, PNG, JPEG. The tool use an .xml format reasonably
simple so interoperability with other tools is also possible with some
development.

Installation
------------

To install `GanttProject`_ in a directory like ``C:\S\GanttProject-2.7``.
In order to do that read the instructions on the `download page`_.
For the sake of simplicity installers are available for various platforms
(e.g. |WindowsInstaller|).

Launching GanttProject
----------------------

The way to launch `GanttProject`_ depends on how the tool has been installed.
With installers you should have create icons. When launched, one way to see
what `GanttProject`_ is all about is to load `house building example`_. In
order to do that use the menu `` Projects >> Open `` and select the
``HouseBuildingSample.gan`` file in the installation directory of the tools.

Documentation
-------------

As far as we know there is no document describing `GanttProject`_.
The tool is nevertheless rather easy to use for someone acquainted
with `project management`_ basics. There is a extended demonstration
in the form of a 15' video |gantt-demo|. The `house building example`_
is also a valuable resource for learning how to use `GanttProject`_.

You may also want to have a look at the following *unofficial* documents
created by people outside of the project:

* "Apprendre Gantt project Ver 2.6" |gantt-apprendre| by Lycée du Dauphiné DD & JPG
    This tutorial, in french, is rather good.

* "GandttProject Handbook 0.52" |gantt-handbook52| by alexandre thomas.
    This handbook is rather obsolete and do not contains too much
    information.

Example
-------

.. _`house building example`:

`GanttProject`_ is delivered with an example of "house building" project.
This project is store in the ``HouseBuildingSample.gan``
|gantt-house-building| file in the root of the installation directory.





.. .........................................................................

.. |gantt-house-building| replace::
    (:download:`local<docs/HouseBuildingSample.gan>`)

.. |gantt-apprendre| replace::
    (:download:`local<docs/apprendre-gantt-project-version-26-vers-17janv2014.pdf>`,
    `web <http://eduscol.education.fr/sti/sites/eduscol.education.fr.sti/files/ressources/pedagogiques/3364/3364-tutoriel-gantt-project-version-26-vers-17janv2014.pdf>`__)

.. |gantt-handbook52| replace::
    (:download:`local<docs/ganttproject-handbook52.pdf>`,
    `web <http://www-mdp.eng.cam.ac.uk/web/CD/engapps/project/ganttprojec.pdf>`__)

.. |gantt-demo| replace::
    (`youtube <https://www.youtube.com/watch?v=5rHCSa5ad34>`__)

.. _`download page`:
    http://www.ganttproject.biz/download.php

.. |WindowsInstaller| replace::
    (:download:`local<../../res/ganttproject/downloads/Win/ganttproject-2.7-r1891.exe>`,
    `web <http://www.ganttproject.biz/download#windows>`__)

.. _`installing from zip`: https://code.google.com/p/ganttproject/wiki/InstallingFromZIPArchive


.. _`GanttProject` : http://www.ganttproject.biz/
.. _`project management`: http://en.wikipedia.org/wiki/Project_management
.. _`gantt models`: http://en.wikipedia.org/wiki/Gantt_chart
.. _`pert models`: http://en.wikipedia.org/wiki/Program_evaluation_and_review_technique
.. _`resource allocation models`: http://en.wikipedia.org/wiki/Resource_allocation
