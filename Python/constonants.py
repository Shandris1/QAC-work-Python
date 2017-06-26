TextString1 = "QA Consulting"
TextString2 = "Office for national statistics"
for x in TextString1:
    #print (x)
    if x == "A" or x == "E" or x == "I" or x == "O" or x == "U" or x == "Y" or x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "y":
        print(x)
for x in TextString2:
    #print (x)
    if x == "A" or x == "E" or x == "I" or x == "O" or x == "U" or x == "Y" or x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "y":
        pass
    else:
        print(x)
