@SET PACKAGE=checkstyle
@SET TDIR=CheckStyle
@SET SOURCE=%SCRIBETOOLS%\%TDIR%
@SET TARGET=res\%PACKAGE%\%TDIR%
@mkdir %TARGET%
copy %SOURCE%\checkstyle.cmd %TARGET%
copy %SOURCE%\checkstyle.sh %TARGET%