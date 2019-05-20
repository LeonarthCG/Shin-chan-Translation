import os
import os.path

characterDict = {
" ": " 0",
"[invalid]": " 1",
"0": " 25",
"1": " 2",
"2": " 3",
"3": " 4",
"4": " 5",
"5": " 6",
"6": " 7",
"7": " 8",
"8": " 9",
"9": " 10",
"A": " 11",
"B": " 12",
"C": " 13",
"D": " 14",
"E": " 15",
"F": " 16",
"G": " 17",
"H": " 18",
"I": " 19",
"J": " 20",
"K": " 21",
"L": " 22",
"M": " 23",
"N": " 24",
"O": " 25",
"P": " 26",
"Q": " 27",
"R": " 28",
"S": " 29",
"T": " 30",
"U": " 31",
"V": " 32",
"W": " 33",
"X": " 34",
"Y": " 35",
"Z": " 36",
"a": " 37",
"b": " 38",
"c": " 39",
"d": " 40",
"e": " 41",
"f": " 42",
"g": " 43",
"h": " 44",
"i": " 45",
"j": " 46",
"k": " 47",
"l": " 48",
"m": " 49",
"n": " 50",
"o": " 51",
"p": " 52",
"q": " 53",
"r": " 54",
"s": " 55",
"t": " 56",
"u": " 57",
"v": " 58",
"w": " 59",
"x": " 60",
"y": " 61",
"z": " 62",
"Á": " 63",
"É": " 64",
"Í": " 65",
"Ñ": " 66",
"Ó": " 67",
"Ú": " 68",
"Ü": " 69",
"á": " 70",
"é": " 71",
"í": " 72",
"ñ": " 73",
"ó": " 74",
"ú": " 75",
"ü": " 76",
"€": " 77",
"$": " 78",
"@": " 79",
"©": " 80",
"®": " 81",
"™": " 82",
"«": " 83",
"»": " 84",
"[quote]": " 85",
"'": " 86",
"‘": " 87",
"’": " 88",
"“": " 89",
"”": " 90",
".": " 91",
"…": " 92",
":": " 93",
";": " 94",
",": " 95",
"¡": " 96",
"!": " 97",
"?": " 98",
"¿": " 99",
"(": " 100",
")": " 101",
"[[]": " 102",
"[]]": " 103",
"&": " 104",
"°": " 105",
"#": " 106",
"%": " 107",
"=": " 108",
"+": " 109",
"-": " 110",
"*": " 111",
"[/]": " 112",
"[\]": " 113",
"<": " 114",
">": " 115",
"_": " 116",
"[uparrowchar]": " 118",
"[downarrowchar]": " 119",
"[leftarrowchar]": " 120",
"[rightarrowchar]": " 121",
"ª": " 122",
"[heartchar]": " 123",
"[songchar]": " 124",
"~": " 125",
"¨": " 126",
"×": " 127",
"[0x8000]": " 0x8000",
"[0x8001]": " 0x8001",
"[0x8002]": " 0x8002",
"[0x8003]": " 0x8003",
"[0x8004]": " 0x8004",
"[0x8005]": " 0x8005",
"[0x8006]": " 0x8006",
"[0x8007]": " 0x8007",
"[0x8008]": " 0x8008",
"[0x8009]": " 0x8009",
"[0x800a]": " 0x800a",
"[0x800b]": " 0x800b",
"[0x800c]": " 0x800c",
"[0x800d]": " 0x800d",
"[0x800e]": " 0x800e",
"[0x800f]": " 0x800f",
"[0x8010]": " 0x8000",
"[0x8011]": " 0x8001",
"[0x8012]": " 0x8002",
"[0x8013]": " 0x8003",
"[0x8014]": " 0x8004",
"[0x8015]": " 0x8005",
"[0x8016]": " 0x8006",
"[0x8017]": " 0x8007",
"[0x8018]": " 0x8008",
"[0x8019]": " 0x8009",
"[0x801a]": " 0x800a",
"[0x801b]": " 0x800b",
"[0x801c]": " 0x800c",
"[0x801d]": " 0x800d",
"[0x801e]": " 0x800e",
"[0x801f]": " 0x800f",
"[0x8020]": " 0x8000",
"[0x8021]": " 0x8001",
"[0x8022]": " 0x8002",
"[0x8023]": " 0x8003",
"[0x8024]": " 0x8004",
"[0x8025]": " 0x8005",
"[0x8026]": " 0x8006",
"[0x8027]": " 0x8007",
"[0x8028]": " 0x8008",
"[0x8029]": " 0x8009",
"[0x802a]": " 0x800a",
"[0x802b]": " 0x800b",
"[0x802c]": " 0x800c",
"[0x802d]": " 0x800d",
"[0x802e]": " 0x800e",
"[0x802f]": " 0x800f",
"\n": "\n"
}

codeDic = {
"[0x8000]": " 0x8000",
"[0x8001]": " 0x8001",
"[0x8002]": " 0x8002",
"[0x8003]": " 0x8003",
"[0x8004]": " 0x8004",
"[0x8005]": " 0x8005",
"[0x8006]": " 0x8006",
"[0x8007]": " 0x8007",
"[0x8008]": " 0x8008",
"[0x8009]": " 0x8009",
"[0x800a]": " 0x800a",
"[0x800b]": " 0x800b",
"[0x800c]": " 0x800c",
"[0x800d]": " 0x800d",
"[0x800e]": " 0x800e",
"[0x800f]": " 0x800f",
"[0x8010]": " 0x8000",
"[0x8011]": " 0x8001",
"[0x8012]": " 0x8002",
"[0x8013]": " 0x8003",
"[0x8014]": " 0x8004",
"[0x8015]": " 0x8005",
"[0x8016]": " 0x8006",
"[0x8017]": " 0x8007",
"[0x8018]": " 0x8008",
"[0x8019]": " 0x8009",
"[0x801a]": " 0x800a",
"[0x801b]": " 0x800b",
"[0x801c]": " 0x800c",
"[0x801d]": " 0x800d",
"[0x801e]": " 0x800e",
"[0x801f]": " 0x800f",
"[0x8020]": " 0x8000",
"[0x8021]": " 0x8001",
"[0x8022]": " 0x8002",
"[0x8023]": " 0x8003",
"[0x8024]": " 0x8004",
"[0x8025]": " 0x8005",
"[0x8026]": " 0x8006",
"[0x8027]": " 0x8007",
"[0x8028]": " 0x8008",
"[0x8029]": " 0x8009",
"[0x802a]": " 0x800a",
"[0x802b]": " 0x800b",
"[0x802c]": " 0x800c",
"[0x802d]": " 0x800d",
"[0x802e]": " 0x800e",
"[0x802f]": " 0x800f",
"\n": "\n"
}

def parse(oldfile,newfile,label,oldlabel,offset):
	error = 0
	output = []
	w = open(newfile,"w+")
	output.append("PUSH; ORG "+str(offset)+"; POIN "+label+"; POP\n")
	output.append("ALIGN 4\n")
	output.append(label+":\n")
	i = 0
	with open(oldlabel, 'r') as f:
		for line in f:
			output.append("POIN "+label+"_"+str(i)+"\n")
			i = i+1
	output.append("WORD 0\n")
	i = 0
	for line in oldfile:
		output.append("ALIGN 4\n")
		output.append(label+"_"+str(i)+":\n")
		output.append("SHORT ")
		line = line.replace("\n","")
		line = stringToDict(line)
		if line == "too big":
			error = 1
		elif line == "no end":
			error = 2
		output.append(line)
		output.append("\n")
		i = i+1
	if error == 0:
		for string in output:
			w.write(string)
	elif error == 1:
		w.write("ERROR \"Width Error: "+oldlabel+"\"")
	elif error == 2:
		w.write("ERROR \"Terminator Error: "+oldlabel+"\"")
	return

def parseName(oldfile,newfile,label,oldlabel,offset):
	error = 0
	output = []
	w = open(newfile,"w+")
	output.append("PUSH; ORG "+str(offset)+"; POIN "+label+"; POP\n")
	output.append("ALIGN 4\n")
	i = 0
	for line in oldfile:
		output.append(label+":\n")
		output.append("SHORT ")
		line = line.replace("\n","")
		line = stringToDict(line)
		if line == "too big":
			error = 1
		elif line == "no end":
			error = 2
		output.append(line)
		output.append("\n")
		i = i+1
	if error == 0:
		for string in output:
			w.write(string)
	elif error == 1:
		w.write("ERROR \"Width Error: "+oldlabel+"\"")
	elif error == 2:
		w.write("ERROR \"Terminator Error: "+oldlabel+"\"")
	return
	
def parseMenu(oldfile,newfile,label,oldlabel,offset):
	error = 0
	output = []
	w = open(newfile,"w+")
	output.append("PUSH; ORG "+str(offset)+"; POIN "+label+"; POP\n")
	output.append("ALIGN 4\n")
	i = 0
	for line in oldfile:
		output.append(label+":\n")
		output.append("SHORT ")
		line = line.replace("\n","")
		line = stringToDictMenu(line)
		if line == "too big":
			error = 1
		elif line == "no end":
			error = 2
		output.append(line)
		output.append("\n")
		i = i+1
	if error == 0:
		for string in output:
			w.write(string)
	elif error == 1:
		w.write("ERROR \"Width Error: "+oldlabel+"\"")
	elif error == 2:
		w.write("ERROR \"Terminator Error: "+oldlabel+"\"")
	return

def stringToDict(string):
	result = ""
	sample = ""
	lastsample = ""
	endofstring = 0
	size = 0
	for i in range(0,len(string)):
		sample = sample+string[i]
		if sample in characterDict:
			if (sample == " ")&(lastsample == " ")&(endofstring == 0):
				size = size-1
				endofstring = 1
			elif (sample in codeDic)&(lastsample == " ")&(endofstring == 0):
				size = size-1
				endofstring = 1
			elif sample in codeDic:
				endofstring = 1
			elif (endofstring == 0)&(sample not in codeDic):
				size = size+1
			result = result+characterDict.get(sample)
			lastsample = sample
			sample = ""
	if endofstring == 0:
		#print(str(size)+" "+string)
		result = "no end"
	elif size > 25:
		#print(str(size)+" "+string)
		result = "too big"
	return(result)
	
def stringToDictMenu(string):
	result = ""
	sample = ""
	lastsample = ""
	endofstring = 0
	size = 0
	for i in range(0,len(string)):
		sample = sample+string[i]
		if sample in characterDict:
			if (sample == " ")&(lastsample == " ")&(endofstring == 0):
				size = size-1
				endofstring = 1
			elif (sample in codeDic)&(lastsample == " ")&(endofstring == 0):
				size = size-1
				endofstring = 1
			elif sample in codeDic:
				endofstring = 1
			elif (endofstring == 0)&(sample not in codeDic):
				size = size+1
			result = result+characterDict.get(sample)
			lastsample = sample
			sample = ""
	if endofstring == 0:
		#print(str(size)+" "+string)
		result = "no end"
	elif size > 24:
		#print(str(size)+" "+string)
		result = "too big"
	return(result)

for dirpath, dirnames, filenames in os.walk(".\Translation\ItemGet"):
	i = 0
	for filename in [f for f in filenames if f.endswith(".txt")]:
		newlabel = "ItemGet"+str(i)
		offset = 4857864+(4*i)
		parse(open(os.path.join(dirpath, filename)),"Parsed\\ItemGet\\"+filename,newlabel,"Translation\\ItemGet\\"+filename,offset)
		i = i+1

for dirpath, dirnames, filenames in os.walk(".\Translation\\NPC"):
	i = 0
	for filename in [f for f in filenames if f.endswith(".txt")]:
		newlabel = "NPC"+str(i)
		offset = 4853612+(4*i)
		parse(open(os.path.join(dirpath, filename)),"Parsed\\NPC\\"+filename,newlabel,"Translation\\NPC\\"+filename,offset)
		i = i+1

for dirpath, dirnames, filenames in os.walk(".\Translation\Plot"):
	i = 0
	for filename in [f for f in filenames if f.endswith(".txt")]:
		newlabel = "Plot"+str(i)
		offset = 4869340+(4*i)
		parse(open(os.path.join(dirpath, filename)),"Parsed\\Plot\\"+filename,newlabel,"Translation\\Plot\\"+filename,offset)
		i = i+1

for dirpath, dirnames, filenames in os.walk(".\Translation\\Names"):
	i = 0
	for filename in [f for f in filenames if f.endswith(".txt")]:
		newlabel = "Names"+str(i)
		offset = 4842720+(4*i)
		parseName(open(os.path.join(dirpath, filename)),"Parsed\\Names\\"+filename,newlabel,"Translation\\Names\\"+filename,offset)
		i = i+1

for dirpath, dirnames, filenames in os.walk(".\Translation\\Menu"):
	i = 0
	for filename in [f for f in filenames if f.endswith(".txt")]:
		skip = 0
		for line in open(os.path.join(dirpath, filename)):
			if line == ("j[0xea00]"):
				skip = 1
		if skip == 0:
			newlabel = "Menu"+str(i)
			offset = 4801544+(4*i)
			parseMenu(open(os.path.join(dirpath, filename)),"Parsed\\Menu\\"+filename,newlabel,"Translation\\Menu\\"+filename,offset)
		i = i+1

w = open("Installer.event","w+")

for dirpath, dirnames, filenames in os.walk(".\Translation\ItemGet"):
	for filename in [f for f in filenames if f.endswith(".txt")]:
		w.write("#include \""+"Parsed\\ItemGet\\"+filename+"\"\n")
		
for dirpath, dirnames, filenames in os.walk(".\Translation\\NPC"):
	for filename in [f for f in filenames if f.endswith(".txt")]:
		w.write("#include \""+"Parsed\\NPC\\"+filename+"\"\n")
		
for dirpath, dirnames, filenames in os.walk(".\Translation\Plot"):
	for filename in [f for f in filenames if f.endswith(".txt")]:
		w.write("#include \""+"Parsed\\Plot\\"+filename+"\"\n")
		
for dirpath, dirnames, filenames in os.walk(".\Translation\\Names"):
	for filename in [f for f in filenames if f.endswith(".txt")]:
		w.write("#include \""+"Parsed\\Names\\"+filename+"\"\n")

for dirpath, dirnames, filenames in os.walk(".\Translation\\Menu"):
	for filename in [f for f in filenames if f.endswith(".txt")]:
		skip = 0
		for line in open(os.path.join(dirpath, filename)):
			if line == ("j[0xea00]"):
				skip = 1
		if skip == 0:
			w.write("#include \""+"Parsed\\Menu\\"+filename+"\"\n")

