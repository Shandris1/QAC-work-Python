GivenString = "AAbazzz"
counter = 0
for x in range(64, 92):

    counter = 0
    for y in GivenString:
        if int((ord(y))) == x or x + 32 == int((ord(y))):
            counter = counter + 1
        if counter != 0:
            print("%s = %d" % (chr(x), counter))
