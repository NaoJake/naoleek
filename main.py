# -*- encoding: UTF-8 -*-

"""Cartesian control: Arm trajectory example"""
from naoqi import ALBroker, ALProxy
from bin.process.hangman import hangmanInit

robotIp = "172.16.6.117"
robotPort = 9559
motionProxy = None
myBroker = ALBroker("myBroker", "0.0.0.0", 0, robotIp, robotPort)

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
        motion = ALProxy("ALMotion", robotIP, robotPort)
        motion.angleInterpolationBezier(names, times, keys)
    except BaseException as err:
        print(err)


def main(robotIP, robotPort):
    """ Example showing a path of two positions
    Warning: Needs a PoseInit before executing
    """

    # Init proxies.
    try:
        global motionProxy
        motionProxy = ALProxy("ALMotion", robotIP, robotPort)
    except Exception as e:
        print("Could not create proxy to ALMotion \n Error was : ", e)

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, robotPort)
    except Exception as e:
        print("Could not create proxy to ALRobotPosture")
        print("Error was: ", e)


    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    customInit(robotIP)
    try:
        sayProxy = ALProxy("ALTextToSpeech", robotIP, robotPort)
        ledProxy = ALProxy("ALLeds", robotIP, robotPort)
    except Exception as e:
        print("Could not create proxy to ALRobotPosture")
        print("Error was: ", e)

    hangmanInit.playGame(sayProxy, ledProxy, motionProxy)


if __name__ == "__main__":

    #if len(sys.argv) <= 1:
    #    print("Usage python motion_cartesianArm1.py robotIP (optional default: 127.0.0.1)")
    #else:
    #    robotIp = sys.argv[1]

    main(robotIp, robotPort)
