@echo off

:: unpack
rmdir /s /q res
mkdir res
quickbms\quickbms_4gb_files.exe "quickbms\wartales.bms" "res.pak" "res"

:: copy & paste
del /f /q res\lang\export_zh.xml
del /f /q res\lang\texts_zh.xml
copy trans\export_zh.xml res\lang\export_zh.xml
copy trans\texts_zh.xml res\lang\texts_zh.xml

:: repack
quickbms\quickbms_4gb_files.exe -w -r -r "quickbms\wartales.bms" "res.pak" "res"

:: cleanup
rmdir /s /q res

pause