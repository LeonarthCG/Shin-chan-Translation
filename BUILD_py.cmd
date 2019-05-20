cd "%~dp0Text"

py "parser.py"

cd %~dp0

copy "%~dp0\Text\rom_clean.gba" rom_translated.gba

cd "%~dp0Event Assembler"

Core A FE8 "-output:%~dp0rom_translated.gba" "-input:%~dp0ROM Buildfile.event"

cd "%~dp0ups"

ups diff -b "%~dp0\Text\rom_clean.gba" -m "%~dp0rom_translated.gba" -o "%~dp0patch.ups"

pause
