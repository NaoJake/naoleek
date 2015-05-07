# -*- encoding: UTF-8 -*-

"""Cartesian control: Arm trajectory example"""

import sys
import motion
import almath
from naoqi import ALProxy


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def customInit(robotIP):
    # Choregraphe bezier export in Python.
    names = list()
    times = list()
    keys = list()

    ctime = 2

    names.append("HeadPitch")
    times.append([ctime])
    keys.append([[-0.17, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([ctime])
    keys.append([[0, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([ctime])
    keys.append([[0.095066, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([ctime])
    keys.append([[-0.12147, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([ctime])
    keys.append([[-0.421516, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([ctime])
    keys.append([[-1.20074, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([ctime])
    keys.append([[0.302384, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([ctime])
    keys.append([[0.123486, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([ctime])
    keys.append([[0.0988769, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([ctime])
    keys.append([[-0.17, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([ctime])
    keys.append([[-0.081128, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([ctime])
    keys.append([[1.36925, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([ctime])
    keys.append([[0.2633, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([ctime])
    keys.append([[0.0988521, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([ctime])
    keys.append([[0.0850586, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([ctime])
    keys.append([[0.12147, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([ctime])
    keys.append([[1.46998, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([ctime])
    keys.append([[0.00254518, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([ctime])
    keys.append([[0.04, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([ctime])
    keys.append([[0.123486, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([ctime])
    keys.append([[-0.0988769, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([ctime])
    keys.append([[-0.17, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([ctime])
    keys.append([[-0.081128, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([ctime])
    keys.append([[-0.00823033, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([ctime])
    keys.append([[-0.0128023, [3, -0.106667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([ctime])
    keys.append([[1.57346, [3, -0.106667, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", robotIP, 55506)
        motion.angleInterpolationBezier(names, times, keys)
    except BaseException as err:
        print(err)


def main(robotIP):
    """ Example showing a path of two positions
    Warning: Needs a PoseInit before executing
    """

    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 55506)
    except Exception as e:
        print("Could not create proxy to ALMotion \n Error was : ", e)

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 55506)
    except Exception as e:
        print("Could not create proxy to ALRobotPosture")
        print("Error was: ", e)

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    customInit(robotIP)

    effector = "RArm"
    space = motion.FRAME_ROBOT
    axisMask = almath.AXIS_MASK_VEL  # just control position
    isAbsolute = False

    # Since we are in relative, the current position is zero
    currentPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Define the changes relative to the current position
    dx = 0.03  # translation axis X (meters)
    dy = 0.00  # translation axis Y (meters)
    dz = 0.00  # translation axis Z (meters)
    dwx = 0.00  # rotation axis X (radians)
    dwy = 0.00  # rotation axis Y (radians)
    dwz = 0.00  # rotation axis Z (radians)
    targetPos = [dx, dy, dz, dwx, dwy, dwz]

    # Go to the target and back again
    path = [targetPos, currentPos]
    times = [2.0, 4.0]  # seconds

    motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)


def createLine(effector, space, tabParam):
    dx = tabParam[0]  # translation axis X (meters)
    dy = tabParam[1]  # translation axis Y (meters)
    dz = tabParam[2]  # translation axis Z (meters)
    dwx = tabParam[3]  # rotation axis X (radians)
    dwy = tabParam[4]  # rotation axis Y (radians)
    dwz = tabParam[5]  # rotation axis Z (radians)

    motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, times, isAbsolute)


if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print("Usage python motion_cartesianArm1.py robotIP (optional default: 127.0.0.1)")
    else:
        robotIp = sys.argv[1]

    main(robotIp)
