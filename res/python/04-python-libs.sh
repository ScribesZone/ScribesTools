#!/usr/bin/env bash
echo Check that '(ScribeEnv)' is in the prompt
echo Otherwise *STOP* this script and type 'workon ScribeEnv'
read
pip install -r requirements-common.txt -r requirements-unix.txt
