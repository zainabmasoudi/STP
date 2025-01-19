:: Automate directory creation
:: By: Zainab Masoudi
:: Initial file: 11292024
:: Filename: directory_automation.bat

@echo off
cls
title directory_automation 
echo ******************************
echo creates directories and files as automatically
echo ******************************
echo *** press [ctrl][c] to exit or any key to continue ***
pause
set /p Project_Name=Enter the name of the project, then press [return] 
echo Creating %Project_Name% 
mkdir %Project_Name%
cd %Project_Name%
echo > READEME.md
echo > main.py
mkdir scripts
mkdir templates
mkdir src
mkdir tests
mkdir docs
mkdir images
echo > settings/__init__.py
echo > src/__init__.py
echo > tests/__init__.py
cls
dir
echo "**********************************************"
echo Finished creating project %NAME%
echo "**********************************************"
cd ..
