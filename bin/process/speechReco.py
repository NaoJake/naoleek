__author__ = 'Justine Dewilde'
from data import alphabet
def listenLetter(motion):
    motion.bIsRunning = True
    visualExpression = True
    wordSpotting = True
    audioExpression = True

    try:
        if motion.asr:
            motion.asr.setAudioExpression(audioExpression)
            motion.asr.setVisualExpression(visualExpression)
            motion.asr.pushContexts()
            motion.hasPushed = True
            if motion.asr:
                motion.asr.setVocabulary(alphabet.listLetter.split(';'), wordSpotting)
            motion.memory.subscribeToEvent("WordRecognized", motion.getName(), "onWordRecognized")
            motion.hasSubscribed = True
    except Exception as err:
         print(err)


def onWordRecognized(motion, key, value, message):
        motion.wordRecognized(value[0])
