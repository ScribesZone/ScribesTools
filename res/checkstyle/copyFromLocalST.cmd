@SET PACKAGE=checkstyle
@SET TDIR=CheckStyle
@SET SOURCE=%SCRIBETOOLS%\%TDIR%
@SET TARGET=res\%PACKAGE%\locals
@mkdir %TARGET%
copy %SOURCE%\checkstyle.cmd %TARGET%
copy %SOURCE%\checkstyle.sh %TARGET%