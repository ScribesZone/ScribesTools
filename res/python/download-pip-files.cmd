@SET THIS_DIR=%~dp0
pip install --download %THIS_DIR%\..\pipdownloads virtualenvwrapper-win virtualenvwrapper
pip install --download %THIS_DIR%\..\pipdownloads -r %THIS_DIR%\requirements-common.txt
pip install --download %THIS_DIR%\..\pipdownloads -r %THIS_DIR%\requirements-unix.txt