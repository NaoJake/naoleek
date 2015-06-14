"""
dx  # translation axis X (meters)
dy  # translation axis Y (meters)
dz  # translation axis Z (meters)
dwx # rotation axis X (radians)
dwy # rotation axis Y (radians)
dwz # rotation axis Z (radians)
"""
from bin.process.main import makeMove


def do_horizontal_dash(go_right, full_dash):
    if go_right and full_dash:
        target_pos = [0.013, 0, 0, 0, 0, 0]
    elif go_right and not full_dash:
        target_pos = [0.006, 0, 0, 0, 0, 0]
    elif not go_right and full_dash:
        target_pos = [-0.013, 0, 0, 0, 0, 0]
    else:
        target_pos = [-0.006, 0, 0, 0, 0, 0]

    makeMove(target_pos)



def do_vertical_dash(go_up):
    if go_up:
        target_pos = [0, 0.01, 0, 0, 0, 0]
    else:
        target_pos = [0, -0.01, 0, 0, 0, 0]

    makeMove(target_pos)



def do_diagonal_dash(go_right, go_up):
    if go_right and go_up:
        target_pos = [0.06, 0.01, 0, 0, 0, 0]
    elif go_right and not go_up:
        target_pos = [0.06, -0.01, 0, 0, 0, 0]
    elif not go_right and go_up:
        target_pos = [-0.06, 0.01, 0, 0, 0, 0]
    else:
        target_pos = [-0.06, -0.01, 0, 0, 0, 0]

    makeMove(target_pos)



def do_z_dash(go_up):
    if go_up:
        target_pos = [0, 0, 0.01, 0, 0, 0]
    else:
        target_pos = [0, 0, -0.01, 0, 0, 0]

    makeMove(target_pos)


def do_underletter_dash():
    target_pos = [0.039, 0, 0, 0, 0, 0]
    makeMove(target_pos)
