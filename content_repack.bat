:: @echo off

:: copy fonts
copy fontgen\output\noto_sans_cjk_regular.fnt noto_sans_cjk_regular.fnt
copy fontgen\output\noto_sans_cjk_regular.png noto_sans_cjk_regular.png

:: repack phase 1
quickbms\quickbms.exe "quickbms\wartales_repack_content.bms" "noto_sans_cjk_regular.fnt" ""
del /f /q content.pak
rename content.pak_mod content.pak

:: repack phase 2
quickbms\quickbms.exe "quickbms\wartales_repack_content.bms" "noto_sans_cjk_regular.png" ""
del /f /q content.pak
rename content.pak_mod content.pak

:: cleanup
del /f /q noto_sans_cjk_regular.fnt
del /f /q noto_sans_cjk_regular.png

pause