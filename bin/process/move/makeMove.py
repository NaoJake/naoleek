import almath
import motion

__author__ = 'Justine Dewilde'
def makeMove(targetPos, motionProxy):
    effector = "RArm"
    space = motion.FRAME_ROBOT
    axisMask = almath.AXIS_MASK_VEL  # just control position
    isAbsolute = False

    # Since we are in relative, the
    # current position is zero
    currentPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Go to the target and back again
    path = [targetPos, currentPos]
    times = [2.0, 4.0]  # seconds

    motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)

