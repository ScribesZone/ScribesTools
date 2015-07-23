@SET PACKAGE=schemaspy
@SET TDIR=SchemaSpy
@SET SOURCE=%SCRIBETOOLS%\%TDIR%
@SET TARGET=res\%PACKAGE%\local
@mkdir %TARGET%
copy %SOURCE%\schemaspy.cmd %TARGET%
copy %SOURCE%\schemaspy.sh %TARGET%
copy %SOURCE%\sqlite.properties %TARGET%
