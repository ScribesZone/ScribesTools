@SET BIN=Win\pycharm-community-4.5.3.exe


@SET TARGETDIR=%SCRIBETOOLS%\PyCharmOpen

mkdir %TARGETDIR%
pycharm\downloads\%BIN%

@echo "About to try the installation ..."
@pause
pycharm
