# Shin-chan Adventures in Cinemaland

This is an English translation of "Shinchan Aventuras en Cineland".
The Spanish translation of the game was pretty rough, some of it was clearly translated literally from English (even though there is no English release), the text doesn't always make sense, a lot of it I had to interpret the best I could.
There is also some text left by the devs, although that didn't affect the in-game text, with one exception.
Please, feel free to add to it, edit it or use it as a base for a different translation.

# Build Instructions

1) Download the project folder
2) Download [Event Assembler](http://feuniverse.us/t/event-assembler/1749), which includes the EA Formatting Suite, and extract it in the "Event Assembler" directory.
3) Download [ups] (https://github.com/rameshvarun/ups/releases) and extract the "ups" folder to the root directory.
4) Add your clean ROM of the Spanish version of the game as "Text/rom_clean.gba".
5) Run "BUILD.cmd". If you prefer it, you can run "BUILD_py.cmd" instead, to run the non-exe version of the parser.

Two files should be produced, "rom_translated.gba" and "patch.ups"

# Editing the translation

All of the translated text and images are found in their respective folders.
Anybody can change them and easily rebuild the ROM with the new changes.

You can run "dump.exe" to get all of the text from the original game.
Feel free to use the existing translation and images.

There is some useful stuff in "Graphics/resources" and in "Text/notes.txt".

Some of the text was used as notes by the devs or is empty, you can ignore those files, but do not delete them.

Keep in mind that:
If there are missing folders in "Text/Source", the dump process will fail.
If there are missing folders in "Text/Parsed", the build process will fail.
If there are missing files or folders in "Text/Translation", the build process will fail.
