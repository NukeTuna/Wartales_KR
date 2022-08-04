@echo off

cd fontgen
rmdir /s /q output
mkdir output
fontgen fontinput.json -info -printmissing -verbose

pause