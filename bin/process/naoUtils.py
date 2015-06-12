__author__ = 'Justine Dewilde'
from naoqi import ALProxy
import time

def naoTalk(motion, sentence):
    motion.say(sentence)


def naoLEDSError(motion):
    motion.leds = ALProxy("ALLeds")
    rDuration = 0.05
    motion.leds.post.fadeRGB( "FaceLed0", 0x000000, rDuration )
    motion.leds.post.fadeRGB( "FaceLed1", 0x000000, rDuration )
    motion.leds.post.fadeRGB( "FaceLed2", 0xffffff, rDuration )
    motion.leds.post.fadeRGB( "FaceLed3", 0x000000, rDuration )
    motion.leds.post.fadeRGB( "FaceLed4", 0x000000, rDuration )
    motion.leds.post.fadeRGB( "FaceLed5", 0x000000, rDuration )
    motion.leds.post.fadeRGB( "FaceLed6", 0xffffff, rDuration )
    motion.leds.fadeRGB( "FaceLed7", 0x000000, rDuration )
    time.sleep(0.2)
    motion.leds.fadeRGB( "FaceLeds", 0xffffff, rDuration )
    motion.onDone()