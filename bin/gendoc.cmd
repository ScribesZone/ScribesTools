@echo off
call bin\activate.cmd
REM FIXME:  go to res and python manage.py extract ALL or something like that
cd docs
call make clean
call make.bat html
cd ..

