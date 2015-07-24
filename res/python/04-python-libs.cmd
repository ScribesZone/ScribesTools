@echo Check that '(ScribeEnv)' is in the prompt
@echo Otherwise *STOP* this script and type 'workon ScribeEnv'
@pause

SET PIPDOWNLOADS=pipdownloads
pip install --no-index --find-links=%PIPDOWNLOADS% -r requirements-common.txt
