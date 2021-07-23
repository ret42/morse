#!/usr/bin/python3

#letters

letters = {"a":" \t","b":"\t   ","c":"\t \t ","d":"\t  ","e":" ","f":"  \t ","g":"\t\t ","h":"    ","i":"  ","j":" \t\t\t","k":"\t \t","l":" \t  ","m":"\t\t","n":"\t ","o":"\t\t\t","p":" \t\t ","q":"\t\t \t","r":" \t ","s":"   ","t":"\t","u":"  \t","v":"   \t","w":" \t\t","x":"\t  \t","y":"\t \t\t","z":"\t\t  ","1":" \t\t\t\t","2":"  \t\t\t","3":"   \t\t","4":"    \t","5":"     ","6":"\t    ","7":"\t\t   ","8":"\t\t\t  ","9":"\t\t\t\t ","0":"\t\t\t\t\t",",":"  \t  ",".":" \t \t \t","?":"  \t\t  ",";":"\t \t \t",":":"\t\t\t   ","/":"\t  \t ","+":" \t \t ","-":"\t    \t","=":"\t   \t","!":"\t\t  \t\t","@":" \t\t \t ","(":"\t \t\t ",")":"\t \t\t \t","á":" \t\t \t","ä":" \t \t","é":"  \t  ","ñ":"\t\t \t\t","ö":"\t\t\t ","ü":"  \t\t","'":" \t\t\t\t ","_":"\t    \t"}

#splitletters

splitletters = {"a":" \t\n","b":"\t   \n","c":"\t \t \n","d":"\t  \n","e":" \n","f":"  \t \n","g":"\t\t \n","h":"    \n","i":"  \n","j":" \t\t\t\n","k":"\t \t\n","l":" \t  \n","m":"\t\t\n","n":"\t \n","o":"\t\t\t\n","p":" \t\t \n","q":"\t\t \t\n","r":" \t \n","s":"   \n","t":"\t\n","u":"  \t\n","v":"   \t\n","w":" \t\t\n","x":"\t  \t\n","y":"\t \t\t\n","z":"\t\t  \n","1":" \t\t\t\t\n","2":"  \t\t\t\n","3":"   \t\t\n","4":"    \t\n","5":"     \n","6":"\t    \n","7":"\t\t   \n","8":"\t\t\t  \n","9":"\t\t\t\t \n","0":"\t\t\t\t\t\n",",":"  \t  \n",".":" \t \t \t\n","?":"  \t\t  \n",";":"\t \t \t\n",":":"\t\t\t   \n","/":"\t  \t \n","+":" \t \t \n","-":"\t    \t\n","=":"\t   \t\n","!":"\t\t  \t\t\n","@":" \t\t \t \n","(":"\t \t\t \n",")":"\t \t\t \t\n","á":" \t\t \t\n","ä":" \t \t\n","é":"  \t  \n","ñ":"\t\t \t\t\n","ö":"\t\t\t \n","ü":"  \t\t\n","'":" \t\t\t\t \n","_":"\t    \t\n"}


filename = input("\n[+] Enter the text file name or type a random name for create a file: ")

#Check extension

if filename.endswith(".txt"):
	None
elif filename.endswith(""):
	filename = filename + ".txt"

char = input("\n[+] Type the text you want: ").lower() #Transform the uppercase to lowercase

if " " in char:
	print("\n[X] Morse does not contain space !")
	exit()

yn = input("\n[?] Do you want to display one letter per row ? [Y/N]: ")

#Encode

if yn in ["N", "n"]:
	result = ""
	for i in char:
		result += letters[i]
	with open(filename, "a") as file: #replace a by w if you want to overwrite
		file.write(result)
		file.close()
else:
	result = ""
	for i in char:
		result += splitletters[i]
	with open(filename, "a") as file: #replace a by w if you want to overwrite
		file.write(result)
		file.close()


print("\n[+] Succesfully encoded !")


#Maybe a decoder and more letters (like spanish letters etc...) if I motivated one day
