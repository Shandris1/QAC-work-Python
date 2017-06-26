class ONS():
    """docstring for ons"""

    def message(self):
        print("hello mortals")
        self.add(7, 2)

    def add(self, B, C):
        Answer = B + C
        print("Result %d" % Answer)

Ref = ONS()
Ref.message()
Ref.add(2, 4)
