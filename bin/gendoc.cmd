@echo off
call bin\activate.cmd
call bin\copyFromLocalST.cmd
cd docs
call make clean
call make.bat html
cd ..

