SQLite
======


Installation
------------
Cette partie est optionnelle. Elle permet pour django de consulter le contenu de la base de données créée par sqlite3 avec la commande “manage.py dbshell”. Ce n’est pas nécessaire pour l’exécution du serveur django.
(1) aller à http://www.sqlite.org/download.html
(2) télécharger “command line shell”. Windows: sqlite-shell-win32-x86-3080600.zip sqlite-shell-win32-x86-3080600.zip
(3) extraire le fichier sqlite3 (windows: sqlite3.exe), le copier dans un répertoire
(4) mettre ce répertoire dans le path

Launching sqlite3
-----------------

(5) pour tester:
(5.1) dans un *nouvelle* fenêtre de commande “sqlite3” doit lancer un shell sqlite3
(5.2) “.schema” affiche rien car pas de bd spécifiée, “.quit” permet de sortir
(5.2) aller dans un répertoire de projet django (ou il y a “manage.py” et “db.sqlite3”)


sqlite3 from django
-------------------
(5.3) “python manage.py dbshell” lance le shell
(5.4) “.schema” affiche le schema de la base django, “.quit” permet de sortir

