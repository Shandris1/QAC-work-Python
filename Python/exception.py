class ONS():
    """docstring for ONS"""

    def exception(self):
         try:
            a = b
            try:

                c = b
            finally:
                print("Inner Finally")

        finally:
            print("Outer Finally")

Def = ONS()
Def.exception()
print("The program is over")
