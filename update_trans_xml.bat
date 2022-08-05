@echo off

:: unpack
rmdir /s /q res
mkdir res
quickbms\quickbms_4gb_files.exe "quickbms\wartales.bms" "res.pak" "res"

:: copy & paste
del /f /q trans\export_zh.xml
del /f /q trans\texts_zh.xml
copy res\lang\export_en.xml trans\export_zh.xml
copy res\lang\texts_en.xml trans\texts_zh.xml

:: cleanup
rmdir /s /q res

pause