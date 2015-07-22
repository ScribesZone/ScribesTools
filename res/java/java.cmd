@SET BIN=Win\jdk-8u51-windows-x64.exe

@SET TARGETDIR=%SCRIBETOOLS%\Java

mkdir %TARGETDIR%
mkdir %TARGETDIR%\jre
mkdir %TARGETDIR%\jdk
java\downloads\%BIN%

@echo "About to try the installation ..."
@pause
java -version