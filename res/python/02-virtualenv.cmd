@SET PIPDOWNLOADS=pipdownloads

pip install --no-index --find-links=%PIPDOWNLOADS% virtualenvwrapper-win
@pause

mkdir %SCRIBETOOLS%\PyVEnvs27
mkvirtualenv ScribeEnv
