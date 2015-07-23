@SET PACKAGE=schemacrawler
@SET TDIR=SchemaCrawler
@SET SOURCE=%SCRIBETOOLS%\%TDIR%
@SET TARGET=res\%PACKAGE%\local
@mkdir %TARGET%
copy %SOURCE%\schemacrawler.cmd %TARGET%
copy %SOURCE%\schemacrawler.sh %TARGET%

