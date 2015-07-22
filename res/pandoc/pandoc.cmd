@SET BIN=Win\pandoc-1.15-windows.msi

@SET TARGETDIR=%SCRIBETOOLS%\Pandoc

mkdir %TARGETDIR%
msiexec /i pandoc\downloads\Win\pandoc-1.15-windows.msi ALLUSERS=1 APPLICATIONFOLDER=%SCRIBETOOLS%\Pandoc

@echo "About to try the installation ..."
@pause
pandoc -v