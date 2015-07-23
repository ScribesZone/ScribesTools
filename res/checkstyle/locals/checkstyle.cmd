@SET THIS_DIR=%~dp0
@SET THIS_DIR_ALA_JAVA=%THIS_DIR:\=/%
@java -jar %THIS_DIR_ALA_JAVA%/checkstyle-all.jar %*
