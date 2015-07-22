@SET BIN=Win\graphviz-2.38.msi

@SET THIS_DIR=%~dp0
@SET SOURCEDIR=%THIS_DIR%\..
@SET TARGETDIR=%SCRIBETOOLS%\Graphviz

mkdir %TARGETDIR%
msiexec /i  %SOURCEDIR%\downloads\%BIN% TARGETDIR=%TARGETDIR% ALLUSER=1

@echo "About to try the installation. Should display the version ..."
@pause
dot -V