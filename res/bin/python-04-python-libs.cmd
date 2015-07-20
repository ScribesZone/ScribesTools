@echo Check that '(ScribeEnv)' is in the prompt
@echo Otherwise *STOP* this script and type 'workon ScribeEnv'
@pause

pip install --no-index --find-links=python\pipdownloads -r python\requirements-common.txt
