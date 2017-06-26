class SystemFunctions():

    def RangeCheck(distance):
        if distance <= 5:
            return 1
        else:
            return 0


class Melee(SystemFunctions):
    """docstring for Melee"""

    def Punch(self, hp):
        if SystemFunctions.RangeCheck:
            hp = hp - 1
        else:
            print("missed")
        return hp


class Ranged(SystemFunctions):

    def Throw(self, hp):
        hp = hp - 1
        return hp


class Fighter(Melee):
    """docstring for fighter"""

    def ProficientStrike(self, hp):
        hp = hp - 10
        return hp


bob = Fighter()

print(bob.ProficientStrike(20))
