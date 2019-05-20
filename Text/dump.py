from intelhex import IntelHex
import os

characterTable = [" ",
"[invalid]",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
"Á",
"É",
"Í",
"Ñ",
"Ó",
"Ú",
"Ü",
"á",
"é",
"í",
"ñ",
"ó",
"ú",
"ü",
"€",
"$",
"@",
"©",
"®",
"™",
"«",
"»",
"[quote]",
"'",
"‘",
"’",
"“",
"”",
".",
"…",
":",
";",
",",
"¡",
"!",
"?",
"¿",
"(",
")",
"[[]",
"[]]",
"&",
"°",
"#",
"%",
"=",
"+",
"-",
"*",
"[/]",
"[\]",
"<",
">",
"_",
"O",
"[uparrowchar]",
"[downarrowchar]",
"[leftarrowchar]",
"[rightarrowchar]",
"ª",
"[heartchar]",
"[songchar]",
"~",
"¨",
"×",
"O",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" ",
" "]

ih = IntelHex()
ih.fromfile('rom_clean.gba',format='bin')

def pointer(rom,offset):
	result = (rom[offset+0])+(rom[offset+1]*256)+(rom[offset+2]*256*256)+(rom[offset+3]*256*256*256)
	result = result&33554431
	return(result)
	
def short(file,offset):
	result = (file[offset+0])+(file[offset+1]*256)
	return(result)

def dump(rom,offset):
	result = ""
	x = 0
	end = 0
	while end == 0:
		if short(rom,offset+(x*2)) < 32768:
			result = result+(characterTable[short(rom,offset+(x*2))])
		else:
			result = result+"["+str(hex(short(rom,offset+(x*2))))+"]"
			end = 1
		x = x+1
	return(result)

table = 4857864
i = 0
while i < 119: #ItemGet
	currentText = pointer(ih,table+(4*i))
	#make the file
	if i < 10:
		dir = str(str(0)+str(0)+str(i))
	elif i < 100:
		dir = str(str(0)+str(i))
	else:
		dir = str(i)
	dir = "Source//ItemGet//"+dir
	w = open(dir+".txt","w+")
	#make the text 
	j = 0
	while pointer(ih,currentText+(4*j)) != 0:
		w.write(str(dump(ih,pointer(ih,currentText+(4*j)))))
		if pointer(ih,currentText+(4*(j+1))) != 0:
			w.write("\n")
		j = j+1
	i = i+1

table = 4801544
i = 0
while i < 80: #Menu
	currentText = pointer(ih,table+(4*i))
	#make the file
	if i < 10:
		dir = str(str(0)+str(0)+str(i))
	elif i < 100:
		dir = str(str(0)+str(i))
	else:
		dir = str(i)
	dir = "Source//Menu//"+dir
	w = open(dir+".txt","w+")
	#make the text 
	w.write(str(dump(ih,currentText)))
	i = i+1

table = 4842720
i = 0
while i < 35: #Names
	currentText = pointer(ih,table+(4*i))
	#make the file
	if i < 10:
		dir = str(str(0)+str(0)+str(i))
	elif i < 100:
		dir = str(str(0)+str(i))
	else:
		dir = str(i)
	dir = "Source//Names//"+dir
	w = open(dir+".txt","w+")
	#make the text 
	w.write(str(dump(ih,currentText)))
	i = i+1


table = 4853612
i = 0
while i < 706: #NPC
	currentText = pointer(ih,table+(4*i))
	#make the file
	if i < 10:
		dir = str(str(0)+str(0)+str(i))
	elif i < 100:
		dir = str(str(0)+str(i))
	else:
		dir = str(i)
	dir = "Source//NPC//"+dir
	w = open(dir+".txt","w+")
	#make the text 
	j = 0
	while pointer(ih,currentText+(4*j)) != 0:
		w.write(str(dump(ih,pointer(ih,currentText+(4*j)))))
		if pointer(ih,currentText+(4*(j+1))) != 0:
			w.write("\n")
		j = j+1
	i = i+1

table = 4869340
i = 0
while i < 630: #Plot
	currentText = pointer(ih,table+(4*i))
	#make the file
	if i < 10:
		dir = str(str(0)+str(0)+str(i))
	elif i < 100:
		dir = str(str(0)+str(i))
	else:
		dir = str(i)
	dir = "Source//Plot//"+dir
	w = open(dir+".txt","w+")
	#make the text 
	j = 0
	while pointer(ih,currentText+(4*j)) != 0:
		w.write(str(dump(ih,pointer(ih,currentText+(4*j)))))
		if pointer(ih,currentText+(4*(j+1))) != 0:
			w.write("\n")
		j = j+1
	i = i+1

