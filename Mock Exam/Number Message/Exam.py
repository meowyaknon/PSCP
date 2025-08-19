""" Number Message """

line = input()

if "13" in line :
    line = line.replace("13", "B")
if "12" in line :
    line = line.replace("12", "R")
if "0" in line :
    line = line.replace("0", "O")
if "5" in line :
    line = line.replace("5", "S")
if "4" in line :
    line = line.replace("4", "A")
if "3" in line :
    line = line.replace("3", "E")
if "1" in line :
    line = line.replace("1", "I")

def main() :
    """ Double check the Decoding """
    save = ""
    for i in line :
        if i.isalpha() or i == " " :
            save += i.upper()

    print(save.strip())
main()
