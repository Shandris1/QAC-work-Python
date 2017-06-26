class Replicate():
    """docstring for Replicate"""

    def __init__(self, A=0, B=0, C=0):
        self.a = A
        self.b = B
        self.c = C

    def __add__(self, other):

        print("2+2")
        return self.a * other.a

china = Replicate(5)
japan = Replicate(7)
print(china + japan)
6 + 4
