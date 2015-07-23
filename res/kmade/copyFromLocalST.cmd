@SET PACKAGE=kmade
@SET TDIR=KMADe
@SET SOURCE=%SCRIBETOOLS%\%TDIR%
@SET TARGET=res\%PACKAGE%\local
@mkdir %TARGET%
copy %SOURCE%\kmade.cmd %TARGET%
copy %SOURCE%\kmade.sh %TARGET%

