@SET PACKAGE=ganttproject
@SET TDIR=GanttProject
@SET SOURCE=%SCRIBETOOLS%\%TDIR%
@SET TARGET=res\%PACKAGE%\local
@mkdir %TARGET%
copy %SOURCE%\ganttproject.cmd %TARGET%


