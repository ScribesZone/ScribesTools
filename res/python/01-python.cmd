@SET BIN=Win\python-2.7.10.msi

@SET DOWNLOADS=downloads
@SET TARGETDIR=%SCRIBETOOLS%\Python27

# REM:  cause a warning in the installer mkdir %TARGETDIR%
msiexec /i  %DOWNLOADS%\%BIN% TARGETDIR=%TARGETDIR% ALLUSER=1 ADDLOCAL=ALL
