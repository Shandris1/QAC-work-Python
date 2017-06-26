class Titan():
    """docstring for Titan"""

    def goding(self):
        print("God hard, play hard")


class Zeus(Titan):
    """docstring for Zeus"""

    def CreateOffspring(self):
        print("Getting down and busy")


class Hades(Titan):
    """docstring for Hades"""

    def HelpingFolksDie(self):
        print("welcome to hel")


class Appolo(Zeus, Hades):
    """docstring for Appolo"""

    def BeingBeautiful(self):
        print("SuperGod")


kid = Appolo()
kid.HelpingFolksDie()
