"""
dx  # translation axis X (meters)
dy  # translation axis Y (meters)
dz  # translation axis Z (meters)
dwx # rotation axis X (radians)
dwy # rotation axis Y (radians)
dwz # rotation axis Z (radians)
"""


def do_horizontal_dash(goLeft, fullDash):
    if goLeft and fullDash:
        target_pos = [0.013, 0, 0, 0, 0, 0]
    elif goLeft and not fullDash:
        target_pos = [-0.006, 0, 0, 0, 0, 0]
    elif not goLeft and fullDash:
        target_pos = [0.013, 0, 0, 0, 0, 0]
    else:
        target_pos = [0.006, 0, 0, 0, 0, 0]

    return target_pos


def do_vertical_dash(goUp, fullDash):
    if goUp:
        target_pos = [0, 0.01, 0, 0, 0, 0]
    else:
        target_pos = [0, 0.01, 0, 0, 0, 0]

    return target_pos

def do_diagonal_dash(goUp, goRight) :
    if goUp and goRight:
        target_pos = [0.06, 0.01, 0, 0, 0, 0]
    elif goUp and not goRight:
        target_pos = [-0.06, -0.01, 0, 0, 0, 0]
    elif not goUp and goRight:
        target_pos = [-0.06, -0.01, 0, 0, 0, 0]
    else:
        target_pos = [-0.06, -0.01, 0, 0, 0, 0]

    return target_pos

"""TODO : finir les 3 methodes du dessus = verif le bon emplacement des matrices"""


# def do_A_D_Dash(direction):
#     if (direction):
#         target_pos = [0.013, 0, 0, 0, 0, 0]
#     else:
#         target_pos = [-0.013, 0, 0, 0, 0, 0]
#
#     return target_pos
#
#
# def do_G1_G2_Dash(direction):
#     if (direction):
#         target_pos = [0.06, 0, 0, 0, 0, 0]
#     else:
#         target_pos = [-0.06, 0, 0, 0, 0, 0]
#
#     return target_pos
#
#
# def do_F_B_E_C_J_M_Dash(direction):
#     if (direction):
#         target_pos = [0, 0.01, 0, 0, 0, 0]
#     else:
#         target_pos = [0, 0.01, 0, 0, 0, 0]
#
#     return target_pos
#
#
# def do_N_K_Dash(direction):
#     if (direction):
#         target_pos = [0.06, 0.01, 0, 0, 0, 0]
#     else:
#         target_pos = [-0.06, -0.01, 0, 0, 0, 0]
#
#     return target_pos
#
#
# def do_H_L_Dash(direction):
#     if (direction):
#         target_pos = [-0.06, -0.01, 0, 0, 0, 0]
#     else:
#         target_pos = [0.06, 0.01, 0, 0, 0, 0]
#
#     return target_pos
#
