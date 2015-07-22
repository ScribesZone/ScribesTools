@SET BIN=Win\Git-1.9.5-preview20150319.exe

@SET THIS_DIR=%~dp0
@SET SOURCEDIR=%THIS_DIR%\..
@SET TARGETDIR=%SCRIBETOOLS%\Git

mkdir %TARGETDIR%
%SOURCEDIR%\downloads\%BIN%

@echo About to try the installation. Should display the help ...
@pause
git help