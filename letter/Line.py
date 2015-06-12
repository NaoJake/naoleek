"""
dx  # translation axis X (meters)
dy  # translation axis Y (meters)
dz  # translation axis Z (meters)
dwx # rotation axis X (radians)
dwy # rotation axis Y (radians)
dwz # rotation axis Z (radians)
"""
from bin.process.main import makeMove


def do_horizontal_dash(goRight, fullDash):
    if goRight and fullDash:
        target_pos = [0.013, 0, 0, 0, 0, 0]
    elif goRight and not fullDash:
        target_pos = [0.006, 0, 0, 0, 0, 0]
    elif not goRight and fullDash:
        target_pos = [-0.013, 0, 0, 0, 0, 0]
    else:
        target_pos = [-0.006, 0, 0, 0, 0, 0]

    makeMove(target_pos)



def do_vertical_dash(goUp):
    if goUp:
        target_pos = [0, 0.01, 0, 0, 0, 0]
    else:
        target_pos = [0, -0.01, 0, 0, 0, 0]

    makeMove(target_pos)



def do_diagonal_dash(goRight, goUp):
    if goRight and goUp:
        target_pos = [0.06, 0.01, 0, 0, 0, 0]
    elif goRight and not goUp:
        target_pos = [0.06, -0.01, 0, 0, 0, 0]
    elif not goRight and goUp:
        target_pos = [-0.06, 0.01, 0, 0, 0, 0]
    else:
        target_pos = [-0.06, -0.01, 0, 0, 0, 0]

    makeMove(target_pos)
