ScribesGit
==========

The purpose of this page is to explain how to use Git and GitHub for course
assignments.

General information about GitHub/Git can be found on in the :ref:`GitHub chapter`.
This page is really about using this general purpose tool for in the particular
context of courses.

Overview
--------
Let us consider as an example the ``aeis`` course of the ``m2r`` school.
with a typical scenario implying the a group ``G12`` in which two students working in pair:

* ``Noe`` and
* ``Babako``.

Obviously **these values has to be replaced by actual values in the commands
presented later**.

All information about the course ``aeis`` is available on github.com. Each group
can see three repositories::

============= ======================================= =============
 Repository   Description                                 Access
============= ======================================= =============
m2r-aeis-info Information and slides about the course Read Only
m2r-aeis-root Assignement skeletons (code, etc.)      Read Only
m2r-aeis-G12  Group repository                        Read/Write
============= ======================================= =============

All repositories lives on GitHub. For instance babako and noe have at
their disposal a "group repository", at ``https://github.com/m2r/m2r-aeis-G12``.
This repository is private so only Noe, Babako and teachers can 
see it when logged in on GitHub.

This repository will be shared by Noe and Babako to work together.
It will contain the final result evaluated at the end of assignments.
In practice Noe and Babako will clone this repository on their local machines,
will work separately on their local repositories and "push" and "pull" modification to 
the "group repository". When the deadline will arrive the content of 
the "group repository" ``m2r-aeis-G12`` will be evaluated.

Scenario
--------
The steps below provides an overview of a possible process. Technical details are 
provided in the next sections.

1.  Noe installs the git toolkit on her machine or uses git it at the university.

2.  Noe first configures git on the local account(s) she uses (on her machine, 
    at the university, or both).

3.  Noe is at the university. She "clones" locally the "group repository"
    from GitHub in a home directory. 
   
4.  Noe "pulls" the assignment skeletons from the
    ``m2r-aeis-root`` repository.
    She gets the different files on her account at the university.

5.  Noe puts Babako and her name in the ``CONTRIBUTORS.md`` file.
    She "commits" and "pushes" this changes to the "group repository" on GitHub.
 
6.  Noe browses the assignments, looks at existing WorkItems,
    makes some first changes in order to start implementing the first assignment.

7.  From time to time Noe "commits" and "pushes" the modifications to the
    "group repository" on GitHub. This will make it possible for her (or Babako)
    to continue to work at home or at the university later). She just has to 
    remember to  "push" the modifications to GitHub at the end of
    each work session. At some point Noe leaves the campus. 

8.  Noe arrives at home and want to continue one her laptop.
    She "pulls" the last modifications from the "group repository"
    and continue working on her laptop.

9.  At anytime Babako can also make a "clone" of the "group repository".
    He will get the last version "pushed" by Noe. He can then work in parallel on 
    other issues for instance.  
   
10. To get the last updates from the "group repository", Noe and Babako
    "pull" the changes regularly. This allows them to incorporate modifications from
    each other. Since they are not fluent with git they avoid to modify the same
    parts of the same file at the same time.
    This helps avoiding  `merge conflicts`_.

11. Deadline is about to arrived. Noe and Babako make sure that all their changes
    have been pushed to the "group repository" on GitHub. They also double check that
    the WorkItems has been updated and that they reflects what has been done.
    
12. The deadline arrives. Nothing has to be delivered: everything is already
    in the "group repository". The work of the group is evaluated though the inspection
    of the content of the "group repository" at the deadline.
    
The following sections explain how to implement such a typical scenario.

Installing Git
--------------

To install git on your machine (if not already installed) have a look at 
the :ref:`Installing the git toolkit section`.

Configuring Git
---------------

You have to configure git once on *each* machine you use. For instance you
may want to configure your account at the university and/or your
account on your personal machine. 

.. attention::
    The values provided in this example MUST be replaced by actual values.

..  code-block:: bash

    #---- configure git -------------------------------------------------------
    # Attributes with --global goes the .gitconfig file.
    # Configure the user associated with contributions (e.g. git push)
    git config --global user.name "Noe ZARWIN"
    git config --global user.email "noezarwin@users.noreply.github.com"

    # Keep the password in memory for 2h
    git config --global credential.helper "cache --timeout=7200"
    # On some machine this method does not work and you will get an error message
    # or a warning after each pull/push. In this case just remove the
    # configuration option above using the following command:
    #    git config --global --unset credential.helper

    # OPTIONAL: Add a proxy ONLY if your machine is behind a firewall
    git config --global http.proxy http://www-cache.ujf-grenoble.fr:3128

    # OPTIONAL: Configure the editor used to edit message. Depends on the OS
    git config --global core.editor "gedit -w -s"  # For ubuntu

    # To see current configuration you can use the "git config -l" command
    # If you want to change something you can always edit the .gitconfig file
    # using the following command (or any editor):
    #   git config --global --edit

Cloning the group repository
----------------------------

To create a local repository on your machine you have to "clone" your
"group repository" (e.g. ``m2r-aeis-G12``) from GitHub. This will create a
local repository on your machine where you can work locally.

.. attention::
    The values provided in this example MUST be replaced by actual values.

..  code-block:: bash

    #---- Clone the "group repository" and into a "local repository" ------------
    # Go to your home directory
    cd  # On unix

    # The "group repository" is at URL like (check this when connected to GitHub)
    # https://<github_account>@github.com/<grade>/<grade>-<class>-<group>.git
    # The GitHub account is specified explicitly (noezarwin below).
    # The following command will ask for the corresponding password.
    # Clone it in the current directory.
    git clone https://noezarwin@github.com/m2r/m2r-aeis-G12.git
    # If you get a message ‘Failed to connect to github.com port 443: Time out’
    # it is most probably that your machine is behind a firewall and that
    # you need to define http.proxy (see the Configuration section above).
    # If you get a message indicating that the repository does not exist
    # this can either be due to:
    # * an error in the url. Check it again and don't miss .git at the end.
    # * a proper read access on the repository might be missing
    #   the given login.
    #   Check this by connecting to GitHub with this login.

    # Enter the newly created directory.
    cd m2r-aeis-G12

Two situations are possible here:

* (1) The **repository is empty**. If you are the first of your group performing
  this series of steps, your group repository could be empty.
  There will be at least the '.git' hidden directory.
  That's ok. Just continue.

* (2) The **repository is initalized**.
  If (an)other(s) member(s) of the group already
  followed these instructions, your group repository will already contains
  their work. This is fine. You will get a non-empty directory. There is
  in particular a ``.git`` hidden directory.
  That's ok. Just continue.

Simply put, this directory contains the "local repository". This directory is
managed through git commands.

Getting assignment skeletons
----------------------------

You now have to configure your repository to get assignment skeletons 
from the "root repository". The "root repository" is maintained by teachers.
This directory contains work definitions, directory structures, file skeletons, 
and so on.

.. attention::
    The values provided in this example MUST be replaced by actual values.

..  code-block:: bash

    #---- Declare the "root directory" and "pull" files from it ---------------
    # Declare the m2r-aeis-root as a remote repository.
    # You can check that you have access to this repository by logging in
    # on GitHub and visiting https://github.com/m2r/m2r-aeis-root .
    # You declaration below should be done only once for each local repository.
    git remote add root https://noezarwin@github.com/m2r/m2r-aeis-root.git

    # If you want to see the list of remote directories use the
    # command "git remote -v". If you made a mistake in the URL and need to change
    # it use the command "git remote set-url <newurl>".

    # "Pull" the assignment skeletons from the "root directory".
    # If an editor opens just enter a message like "get assignment skeletons"
    git pull root master
    # You should now have the assignment skeletons in the local repository.
    # Note that if you get an error at this level this could be either because:
    # * you've made an error in the url above. Use git remote -v to check it.
    #   If there is an error use the following command
    #      git remote set-url root <the-url>
    # * you do not have read access to this repository. Please check this
    #   going on GitHub and check if you see it with your login.

    # You can browse the content of the directory with "ls -la" on unix.
    # There is one directory per assignment.

..  ........
    Browsing Work Definitions
    -------------------------
    Let us call "WorkDefinition" the definition of the tasks to perform
    to complete  assignments. Work definitions are implemented in terms of
    `GitHub issues`_ in the "root repository" as shown in the example below:

    ..  image:: media/WorkDefinitionExample.png
        :align: center

    If you have questions about work definitions, do not hesitate to post a
    a question. Just take care of choosing a title as clear as possible for
    your question.


Changing CONTRIBUTORS.rst
-------------------------

..  One of your first work is likely to be defined by an "WorkDefinition"
    (an issue) most likely entitled ``[WD] Define Repository Contributors``.

You have to fill the ``CONTRIBUTORS.rst`` file in the repository
and to put the information about your group using the format such as below.

::

    === ===== ======= ====================== ======================= ===================== =====================================
     n  group trigram       firstname              lastname              githubAccount                    email
    === ===== ======= ====================== ======================= ===================== =====================================
    1   G12   BST     Babako                 SCHMIDT                 babako12              babako.schmidt@e.ujf-grenoble.fr
    2   G12   NZN     Noe                    ZARWIN                  noezarwin             noezarwin@gmail.com
    === ===== ======= ====================== ======================= ===================== =====================================

There should be one line for each member. The list must be **sorted by lastnames**.
Spaces and blank lines are important in the RST format.

..  attention::
    The values provided in this example MUST be replaced by actual values.

..  code-block:: bash

    #---- Edit CONTRIBUTORS.md, commit and push the change --------------------
    # Use your favorite editor to edit CONTRIBUTORS.md.
    # Enter the data about all group members in the following format.

The fields are the following:

:N:
    The indice of the member in the list. Members must be list
    in alphabetical order on the lastname, then firstname.
:group:
    The group number (e.g. ``G12``).
:trigram:
    Three uppercase letters:

    * the first letter of the firstname
    * the first letter of the lastname
    * the **last** letter of the lastname

    See the quality rule
    `Trigramme <http://scribesquality.readthedocs.org/en/latest/packages/Nomenclature.html#trigramme>`_
    for details about composite names.
:firstname:
    The firstname of the member (e.g. ``Babako``).
:lastname:
    The lastname of member using UPPERCASES$ (e.g. ``SCHMIDT``).
:githubAccount:
    The login used by the member to connect to GitHub.
:email:
    A valid email address.

..  attention::
    The lines must be **sorted by lastnames** (ascending order).
    This is fundamental for defining the ``n`` indice.

    The lastname must be all in uppercases.

    Change the width of columns if you need more space for your name, email, etc.
    A strict alignement is necessary for the .rst processor to parse this table correctly.



..  code-block:: bash

    # Save the file.
    #
    # Add the modified file to the files to be saved in the next commit
    git add .

    # Commit (e.g. save) the changes to the local repository
    git commit -a -m "Set the authors for this repository"

    # Push (e.g. publish) the state of the local repository to github
    git push origin master
    # If you get an error here indicating that there is no such repository
    # this could be because you don't have write access to this repository.
    # Go to GitHub using the login used in the url and check if you can edit
    # files. If not post an issue in the root repository and writing rights
    # will be associated to your account.

The changes should now appear on GitHub "group repository".
Log in to GitHub and go to your group repository (e.g. ``https://github.com/m2gi/m2gi-idm-G12``)
to check.

Making and pushing changes
--------------------------

Time to work and deal with assignments. The process is all about
making changes, committing these changes to the "local repository"
and pushing these changes on GitHub to the "group repository".

..  code-block:: bash

    #---- Making changes, committing and pushing them -------------------------
    # Make some changes.

    # Check which files have changed.
    # Use the "-s" option if you prefer a shorter format.
    git status

    # Add files to be committed. Replace <files> below by actual file names.
    # Use "git add ." to commit the whole directory
    git add <files>

    # Commit the files (save them in the local repository)
    # Provide a useful message instead of <message>.
    git commit -a -m ‘<message>’

    # OPTIONAL: push changes to the "group repository" on GitHub
    # You must do this at the end of a working session if you
    # plan to continue on another machine (at home for instance)
    # or if you want other group members to "see" the changes.
    git push origin master


Pulling changes from the group repo
-----------------------------------
If you work on various machines or if other group members
work in parallel your local repository may not contains
the last changes available on GitHub in the group repository.
In this case you have to "pull" these changes as following.

..  code-block:: bash

    #---- Pulling changes from the group repository on GitHub -----------------
    # Before making a "pull" make sure that you have committed all changes.
    # "origin" refers to the "group repository" on GitHub.
    # The "pull" command download the latest changes from the "group repository"
    # then it try to merge these changes with those made locally.
    git pull origin master

Pulling changes may cause some merge conflicts. 
See `resolving merge conflicts`_ in this case.

Pulling changes from the root repo
----------------------------------
During the course new assignments may be created and/or new material
may be added into an existing assignment, for instance to bring
precision to some tasks or to add additional skeletons. These changes
will be made available through the "root repository" which contains
assignment skeletons. In order to get last updates you just have to 
pull these changes in the same way you pull changes from your
"group repository".

..  code-block:: bash

    # Before making a "pull" make sure that you have committed all changes.
    # "root" refers to the "root repository" on GitHub.
    # This "remote" repository has been declared in the "Getting assignment skeletons"
    # section.
    git pull root master

Pulling changes may cause some merge conflicts. 
See `resolving merge conflicts`_ in this case.


Staying informed
----------------
In GitHub terms, "Watching" a repository means receiving notification when
changes occur to it.

Since you are member of your "group repository" you should automatically receive
notifications for new commits for instance. This is handy to keep in synch 
with other group members. By default you "Watch" this repository but you
can change this by pressing on the "Unwatch" button on GitHub.

If you want to stay informed you may also want to "Watch" the following
repositories.

*   the "info" repository for general information about the course.
    This can be useful to get notified when new slides are added for instance.
    
*   the "root" repository. Register to this repository if you want to
    receive information about assignments, get notification when questions are
    posted, etc.
    
.. note::
    If you receive too much notifications you can change the settings at any moment.

Questions/Bugs/...?
-------------------
If you found a bug in an assignement, if you have some comments or 
or have a question about the course please post an 
[GitHub issue](https://guides.github.com/features/issues/).

Please select the repository that is most suited to your issue:

* If the "issue" is general or related to a particular assignment and
  the question/issue is relevant to other groups, then post the issue in "root"
  repository.
  
* If the "issue" is only related to your group (you and other group member partner)
  please post the issue in your "group" repository (``m2r-aeis-G12`` for instance).
  Use the (!) button in the web interface (see
  [create an issue](https://guides.github.com/features/issues/) for details).
  
If you have some answer to some posted issues, please provide it directly online. 

.. attention::
    Use issues to communicate, not emails.

.. ................................................................................


..  _`merge conflicts` :
    https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/

..  _`resolving merge conflicts`: `merge conflicts`_

..  _`GitHub issues` :
    https://guides.github.com/features/issues/