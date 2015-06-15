__author__ = 'Justine Dewilde'

import time

def naoTalk(motion, sentence):
    motion.say(sentence)

def naoLEDSOther(motion):
    rDuration = 0.05
    motion.post.fadeRGB("FaceLed0", 0x375D81, rDuration)
    motion.post.fadeRGB("FaceLed1", 0x8CC6D7, rDuration)
    motion.post.fadeRGB("FaceLed2", 0x375D81, rDuration)
    motion.post.fadeRGB("FaceLed3", 0x8CC6D7, rDuration)
    motion.post.fadeRGB("FaceLed4", 0x375D81, rDuration)
    motion.post.fadeRGB("FaceLed5", 0x8CC6D7, rDuration)
    motion.post.fadeRGB("FaceLed6", 0x375D81, rDuration)
    motion.fadeRGB("FaceLed7", 0x8CC6D7, rDuration)
    time.sleep(0.2)
    motion.fadeRGB("FaceLeds", 0xffffff, rDuration)


def naoLEDSError(motion):
    rDuration = 0.05
    motion.post.fadeRGB("FaceLed0", 0xFF5B2B, rDuration)
    motion.post.fadeRGB("FaceLed1", 0xB1221C, rDuration)
    motion.post.fadeRGB("FaceLed2", 0xFF5B2B, rDuration)
    motion.post.fadeRGB("FaceLed3", 0xB1221C, rDuration)
    motion.post.fadeRGB("FaceLed4", 0xFF5B2B, rDuration)
    motion.post.fadeRGB("FaceLed5", 0xB1221C, rDuration)
    motion.post.fadeRGB("FaceLed6", 0xFF5B2B, rDuration)
    motion.fadeRGB("FaceLed7", 0xB1221C, rDuration)
    time.sleep(0.2)
    motion.fadeRGB("FaceLeds", 0xffffff, rDuration)


def naoLEDSCorrect(motion):
    rDuration = 0.05
    motion.post.fadeRGB("FaceLed0", 0x78A419, rDuration)
    motion.post.fadeRGB("FaceLed1", 0x8FCF3C, rDuration)
    motion.post.fadeRGB("FaceLed2", 0x78A419, rDuration)
    motion.post.fadeRGB("FaceLed3", 0x8FCF3C, rDuration)
    motion.post.fadeRGB("FaceLed4", 0x78A419, rDuration)
    motion.post.fadeRGB("FaceLed5", 0x8FCF3C, rDuration)
    motion.post.fadeRGB("FaceLed6", 0x78A419, rDuration)
    motion.fadeRGB("FaceLed7", 0x8FCF3C, rDuration)
    time.sleep(0.2)
    motion.fadeRGB("FaceLeds", 0xffffff, rDuration)