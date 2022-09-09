:: This file should be placed in the QGIS root directory, together with the script update_qgis_env.py.
@echo off
:: Find the Python version bundled with QGIS.  This can be Python37, Python38, ..., depending on the QGIS version
FOR /D %%i IN (%~dps0apps\Python*) DO SET PYTHONHOME=%%i
:: Add 'bin' to PATH to find vcruntime.
set PATH=%~dps0bin;%PATH%
%PYTHONHOME%\python3.exe %~dps0update_qgis_env.py %~dps0
echo Adjusted QGIS .env files.
pause
