
def encryptWord(L):
    charascii = ord(L)
    encryptedString = charascii
    return (encryptedString)


# FileLocation = input("LOCATE A FILE FOR ME, MORTAL")
FileLocation = "InputFile.txt"
EncryptedFile = "encryptedFile.txt"
DecryptedFile = "decryptedFile.txt."
F = open(FileLocation, "r")
# F = open("war-and-peace.txt", "r")
W = open(EncryptedFile, "w")
W.close
W = open(EncryptedFile, "a")
Data = F.read()
LetterToReplace = "a"
LetterReplaceWith = "b"
# LetterToReplace = input("Enter what to replace :")
# LetterReplaceWith = input("Enter what to replace the letter to :")
for Char in Data:
    encrypted = int((ord(Char)) ^ 0b0010)
    if encrypted % 2 == 1:
        encrypted = encrypted ^ 0b1000
    else:
        encrypted = encrypted ^ 0b0100
    W.write(chr(encrypted))

F.close
W.close
G = open(EncryptedFile, "r")
H = open(DecryptedFile, "w")
H.close
H = open(DecryptedFile, "a")
DataRead = G.read()
for Char in DataRead:
    #    print(Char)
    encrypted = int((ord(Char)) ^ 0b0010)
    if encrypted % 2 == 1:
        encrypted = encrypted ^ 0b1000
    else:
        encrypted = encrypted ^ 0b0100

    H.write(chr(encrypted))
