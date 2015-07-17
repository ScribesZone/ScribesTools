@SET THIS_DIR=%~dp0
@SET THIS_DIR_ALA_JAVA=%THIS_DIR:\=/%
@SET SC_DIR=%THIS_DIR_ALA_JAVA%/_schemacrawler
@java -classpath %SC_DIR%/lib/*;%SC_DIR% schemacrawler.Main %*
