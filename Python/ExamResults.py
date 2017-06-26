class Results(object):
    """docstring for Results"""

    def __init__(self, x=0, y=0, z=0):
        self.__phy = x
        self.__math = y
        self.__chem = z
        # self.__calculations()
        # self.ShowResults()

    def Assigphy(self, value):
        if value > 0 and value < 150:
            self.__phy = value
        else:
            print("Wrong value")

    def Assigchem(self, value):
        if value > 0 and value < 150:
            self.__chem = value
        else:
            print("Wrong value")

    def Assimathy(self, value):
        if value > 0 and value < 150:
            self.__math = value
        else:
            print("Wrong value")

    def calculations(self):
        self.Total = self.__phy + self.__chem + self.__math
        self.Per = (self.Total / 450) * 100

    def ShowResults(self):
        print(self.Total)
        print(self.Per)

    def Numberpassed(self):
        passed = 0
        if self.__math / 150 * 100 > 60:
            passed = passed + 1
        if self.__phy / 150 * 100 > 60:
            passed = passed + 1
        if self.__chem / 150 * 100 > 60:
            passed = passed + 1
        if passed == 0:
            print("Go home")
        elif passed == 1:
            print("Redo Everything")
        elif passed == 2:
            print("Retake Test")
        elif passed == 3:
            print("Passed everything, well done")
John = Results()
John.Assimathy(140)
John.Assigchem(130)
John.Assigphy(30)
John.calculations()
John.ShowResults()
John.Numberpassed()
