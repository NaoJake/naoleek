from letter.Line import do_vertical_dash, do_horizontal_dash


def createA():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)
    do_horizontal_dash(False, True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)


def createB():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)
    do_horizontal_dash(False, True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)
    do_horizontal_dash(False, True)


def createC():
    do_horizontal_dash(True, True)
    do_horizontal_dash(False, True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)


def createD():

    pass


def createE():
    pass


def createF():
    pass


def createG():
    pass


def createH():
    pass


def createI():
    do_vertical_dash(True)


def createJ():
    pass


def createK():
    pass


def createL():
    pass


def createM():
    pass


def createN():
    pass


def createO():
    pass


def createP():
    pass


def createQ():
    pass


def createR():
    pass


def createS():
    pass


def createT():
    pass


def createU():
    pass


def createV():
    pass


def createW():
    pass


def createX():
    pass


def createY():
    pass


def createZ():
    pass


def dispatcher(input):
    input.upper()

    if input == "A":
        createA()
    elif input == "B":
        createB()
    elif input == "C":
        createC()
    elif input == "D":
        createD()
    elif input == "E":
        createE()
    elif input == "F":
        createF()
    elif input == "G":
        createG()
    elif input == "H":
        createH()
    elif input == "I":
        createI()
    elif input == "J":
        createJ()
    elif input == "K":
        createK()
    elif input == "L":
        createL()
    elif input == "M":
        createM()
    elif input == "N":
        createN()
    elif input == "O":
        createO()
    elif input == "P":
        createP()
    elif input == "Q":
        createQ()
    elif input == "R":
        createR()
    elif input == "S":
        createS()
    elif input == "T":
        createT()
    elif input == "U":
        createU()
    elif input == "V":
        createV()
    elif input == "W":
        createW()
    elif input == "X":
        createX()
    elif input == "Y":
        createY()
    elif input == "Z":
        createZ()
