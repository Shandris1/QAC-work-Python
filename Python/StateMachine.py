def AskForNumbers():  # Returns 2 AskForNumbers
    Number1 = int(input("Enter First No :"))
    Number2 = int(input("Enter Second No :"))
    return (Number1, Number2)


def PrintOptions():
    print("1-Addition")
    print("2-Subtraction")
    print("3-Division")
    print("4-Multiplication")
    print("5-TimesTable")
    print("6-Quit")


def Repeat():
    DesiredOption = input("Do you want to Repeat? Yes/No: ")
    return(DesiredOption)


def Addition():
    Number1, Number2 = AskForNumbers()
    Result = Number1 + Number2
    return Result


def Subtraction():
    Number1, Number2 = AskForNumbers()
    Result = Number1 - Number2
    return Result


def Division():
    Number1, Number2 = AskForNumbers()
    Result = Number1 / Number2
    return Result


def Multiplication():
    Number1, Number2 = AskForNumbers()
    Result = Number1 * Number2
    return Result


def TimesTable():
    StartNumber, EndNumber = AskForNumbers()
    if StartNumber <= EndNumber:
        for x in range(StartNumber, EndNumber + 1):
            print("%d x %d = %d" % (StartNumber, x, StartNumber * x))
    else:
        for x in range(StartNumber, EndNumber - 1, -1):
            print("%d x %d = %d" % (StartNumber, x, StartNumber * x))


def Display(Result):
    print("The Result is ", Result)

choice = 1  # keep track of user choice
choice2 = 0
count = 0  # keep track op options positions
repeat = 1
PrintOptions()
while True:  # loop while program is open
    if repeat == 1:
        choice = int(input("Enter Your Choice :"))
        repeat = 3
    if choice == 1:
        Display(Addition())
    elif choice == 2:
        Display(Subtraction())
    elif choice == 3:
        Display(Division())
    elif choice == 4:
        Display(Multiplication())
    elif choice == 5:
        TimesTable()
        count = count + 10
    elif choice == 6:
        break
    else:
        repeat = 1
    count = count + 3
    if count > 30:  # Display options if they drift offscreen
        count = 0
        PrintOptions()

    while repeat < 0 or repeat > 1:
        choice2 = Repeat()
        # print(choice2)
        if choice2 == "Yes" or choice2 == "Y":
            repeat = 0
        elif choice2 == "No" or choice2 == "N":
            repeat = 1
        else:
            repeat = 3
            print("Invalid choice")
