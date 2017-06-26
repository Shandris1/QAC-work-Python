StartNumber = int(input("enter from number: "))
EndNumber = int(input("enter to number: "))
if StartNumber <= EndNumber:
    for x in range(StartNumber, EndNumber + 1):
        for y in range(1, 11):
            print("%d x %d = %d" % (x, y, x * y))
else:
    for x in range(StartNumber, EndNumber - 1, -1):
        for y in range(1, 11):
            print("%d x %d = %d" % (x, y, x * y))