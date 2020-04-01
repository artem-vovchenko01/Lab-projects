@echo off
for %%f in (%*) do type %%f.txt >> newfile.txt
type newfile.txt > %1.txt

for /f %%i in ("newfile.txt") do set size=%%~zi
if %size% gtr 0 echo Resulting file is not empty
goto :result:

:result:
echo success!
type %1.txt
break>newfile.txt
