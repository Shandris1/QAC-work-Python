

FileLocation = input("LOCATE A FILE FOR ME, MORTAL")
#FileLocation = "war-and-peace.txt"
F = open(FileLocation, "r")
#F = open("war-and-peace.txt", "r")
W = open("Result.txt", "w")
W.close
W = open("Result.txt", "a")
Data = F.read()
LetterToReplace = "T"
LetterReplaceWith = "Liveform Annihilated"
LetterToReplace = input("Enter what to replace :")
LetterReplaceWith = input("Enter what to replace the letter to :")
for Char in Data:
    if Char == LetterToReplace:
        W.write(LetterReplaceWith)
    else:
        W.write(Char)
F.close
W.close
