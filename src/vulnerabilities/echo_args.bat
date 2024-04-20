@echo off
set index=1

:loop
if "%~1"=="" goto :end
echo arg%index%: %1
set /a index+=1
shift
goto :loop

:end