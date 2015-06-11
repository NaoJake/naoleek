from letter.Line import do_vertical_dash, do_horizontal_dash, do_diagonal_dash


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
    do_horizontal_dash(True, True)
    do_horizontal_dash(False, True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_horizontal_dash(False, True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_horizontal_dash(False, True)


def createF():
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_horizontal_dash(False, True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_horizontal_dash(False, True)


def createG():
    pass


def createH():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_vertical_dash(False)
    do_horizontal_dash(True, True)
    do_vertical_dash(True)
    do_vertical_dash(False)
    do_vertical_dash(False)


def createI():
    do_vertical_dash(True)
    do_vertical_dash(True)


def createJ():
    do_horizontal_dash(True, True)
    do_vertical_dash(True)
    do_vertical_dash(True)


def createK():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_vertical_dash(False)
    do_horizontal_dash(True, False)
    do_diagonal_dash(True, True)
    do_diagonal_dash(False, False)
    do_diagonal_dash(True, False)


def createL():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_vertical_dash(False)
    do_vertical_dash(False)
    do_horizontal_dash(True, True)


def createM():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_diagonal_dash(True, False)
    do_diagonal_dash(True, True)
    do_vertical_dash(False)
    do_vertical_dash(False)


def createN():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_diagonal_dash(True, False)
    do_diagonal_dash(True, False)
    do_vertical_dash(True)
    do_vertical_dash(True)


def createO():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)
    do_vertical_dash(False)
    do_horizontal_dash(False, True)

def createP():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)
    do_horizontal_dash(False, True)


def createQ():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)
    do_vertical_dash(False)
    do_horizontal_dash(False, True)
    do_horizontal_dash(True, True)
    do_diagonal_dash(False, True)


def createR():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_horizontal_dash(True, True)
    do_vertical_dash(False)
    do_horizontal_dash(False, False)
    do_diagonal_dash(True, False)


def createS():
    do_diagonal_dash(True, True)
    do_vertical_dash(True)
    do_diagonal_dash(False, True)
    do_vertical_dash(True)
    do_diagonal_dash(True, True)


def createT():
    pass


def createU():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_vertical_dash(False)
    do_vertical_dash(False)
    do_horizontal_dash(True, True)
    do_vertical_dash(True)
    do_vertical_dash(True)


def createV():
    pass


def createW():
    do_vertical_dash(True)
    do_vertical_dash(True)
    do_vertical_dash(False)
    do_vertical_dash(False)
    do_diagonal_dash(True, True)
    do_diagonal_dash(True, False)
    do_vertical_dash(True)
    do_vertical_dash(True)


def createX():
    do_diagonal_dash(True, True)
    do_diagonal_dash(False,True)
    do_diagonal_dash(True, False)
    do_diagonal_dash(True, True)
    do_diagonal_dash(False, False)
    do_diagonal_dash(True, False)


def createY():
    pass


def createZ():
    do_horizontal_dash(True, True)
    do_horizontal_dash(False, True)
    do_diagonal_dash(True, True)
    do_diagonal_dash(True, True)
    do_horizontal_dash(False, True)


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
