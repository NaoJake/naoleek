# -*- encoding: UTF-8 -*-
from letter.Line import do_vertical_dash, do_horizontal_dash, do_diagonal_dash, do_z_dash, do_underletter_dash


def createA(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createB(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createC(motionProxy):
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createD(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_diagonal_dash(False, False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createE(motionProxy):
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createF(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createG(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(False, False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createH(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createI(motionProxy):
    do_z_dash(True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_z_dash(False, motionProxy)


def createJ(motionProxy):
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_z_dash(False, motionProxy)


def createK(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    do_diagonal_dash(False, False, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createL(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createM(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createN(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createO(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createP(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createQ(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_diagonal_dash(False, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createR(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(False, False, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createS(motionProxy):
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createT(motionProxy):
    do_z_dash(True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_horizontal_dash(False, False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createU(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createV(motionProxy):
    do_z_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_z_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    do_vertical_dash(True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createW(motionProxy):
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createX(motionProxy):
    do_diagonal_dash(True, True, motionProxy)
    do_diagonal_dash(False, True, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    do_diagonal_dash(False, False, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createY(motionProxy):
    do_z_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_z_dash(False, motionProxy)
    do_diagonal_dash(True, False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(True, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def createZ(motionProxy):
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    do_diagonal_dash(True, True, motionProxy)
    do_horizontal_dash(False, True, motionProxy)
    #fin lettre

    do_z_dash(True, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_vertical_dash(False, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, True, motionProxy)
    do_horizontal_dash(True, False, motionProxy)
    do_z_dash(False, motionProxy)


def dispatcher(input, motionProxy):
    """
    A la fin d'une lettre on doit se retrouver au début du tiret de la lettre suivante
    :param input: la lettre à écrire
    """
    input.upper()

    if input == "A":
        createA(motionProxy)
    elif input == "B":
        createB(motionProxy)
    elif input == "C":
        createC(motionProxy)
    elif input == "D":
        createD(motionProxy)
    elif input == "E":
        createE(motionProxy)
    elif input == "F":
        createF(motionProxy)
    elif input == "G":
        createG(motionProxy)
    elif input == "H":
        createH(motionProxy)
    elif input == "I":
        createI(motionProxy)
    elif input == "J":
        createJ(motionProxy)
    elif input == "K":
        createK(motionProxy)
    elif input == "L":
        createL(motionProxy)
    elif input == "M":
        createM(motionProxy)
    elif input == "N":
        createN(motionProxy)
    elif input == "O":
        createO(motionProxy)
    elif input == "P":
        createP(motionProxy)
    elif input == "Q":
        createQ(motionProxy)
    elif input == "R":
        createR(motionProxy)
    elif input == "S":
        createS(motionProxy)
    elif input == "T":
        createT(motionProxy)
    elif input == "U":
        createU(motionProxy)
    elif input == "V":
        createV(motionProxy)
    elif input == "W":
        createW(motionProxy)
    elif input == "X":
        createX(motionProxy)
    elif input == "Y":
        createY(motionProxy)
    elif input == "Z":
        createZ(motionProxy)


def make_initial_dash(nb_dash, motionProxy):
    print("ecriture dash")
    for i in range(nb_dash):
        print(i)
        do_underletter_dash(True, motionProxy)
        do_z_dash(True, motionProxy)
        do_horizontal_dash(True, False, motionProxy)
        do_z_dash(False, motionProxy)

    #retour au début
    print("dash terminé, retour au début")
    do_z_dash(True, motionProxy)
    for i in range(nb_dash):
        print(i)
        do_horizontal_dash(False, False, motionProxy)
        do_underletter_dash(False, motionProxy)
    do_z_dash(False, motionProxy)
    print("rendu au début")


def write_at_position(letter, position, motionProxy):
    current_position = 0
    for i in range(len(position)):
        print("current position : " + str(current_position))
        do_z_dash(True, motionProxy)
        for j in range(current_position, position[i]):
            current_position += 1
            do_underletter_dash(True, motionProxy)
            do_horizontal_dash(True, False, motionProxy)
        do_horizontal_dash(True, True, motionProxy)
        do_vertical_dash(True, motionProxy)
        do_z_dash(False, motionProxy)
        dispatcher(letter, motionProxy)
        current_position += 1

    #retour au début
    do_z_dash(True, motionProxy)
    for k in range(current_position):
        do_horizontal_dash(False, True, motionProxy)
        do_underletter_dash(False, motionProxy)
    do_z_dash(False, motionProxy)
