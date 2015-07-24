@echo Check that '(ScribeEnv)' is in the prompt
@echo Otherwise *STOP* this script and type 'workon ScribeEnv'
@pause

@SET DOWNLOADS=downloads

easy_install %DOWNLOADS%\Win\pywin32-219.win32-py2.7.exe
@pause

pip install %DOWNLOADS%\Win\pygraphviz-1.3rc2-cp27-none-win32.whl
@pause

easy_install.exe %DOWNLOADS%\Win\pycrypto-2.6.win32-py2.7.exe
