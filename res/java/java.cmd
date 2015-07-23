

mkdir %TARGETDIR%
mkdir %TARGETDIR%\jre
mkdir %TARGETDIR%\jdk
java\downloads\%BIN%

@echo "About to try the installation ..."
@pause
java -version