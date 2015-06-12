__author__ = 'Justine Dewilde'

from naoqi import ALProxy
from bin.process.hangman import hangmanGame
from bin.process.strUtils import getPositionOfLetterInWord

def playGame(motion):
    "fonction permettant de lancer le jeu"

    try:
        welcome = "Bonjour, nous allons jouer au pendu ! Je vais d'abord choisir un mot"
        #motion.say(welcome)
        print(welcome)
        hmGame = hangmanGame.HangmanGame()
        randomWord = hmGame.getWordToFind()
        motion.say("Voila ! Ce mot a {0} lettres".format(str(len(randomWord))))
        motion.say("C'est parti !")
        print("Voila ! Ce mot a {0} lettres".format(str(len(randomWord))))
        print("C'est parti !")
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #ajouter la partie permettant d'ecrire les traits : nbr de traits > (len(randomWord)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(randomWord)

        #Partie
        while not(hmGame.didNaoLost()) and not(hmGame.didNaoWin()):
            randomLetter = hmGame.getRandomLetter()
            hmGame.putLetter(randomLetter)
            if hmGame.correctLetter(randomLetter):
                motion.say("Bien ! La lettre {0} fait partie du mot".format(str(randomLetter)))
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #fonction a mettre ici : nao ecrit la lettre : lettre > randomLetter & liste des positions :  getPositionOfLetterInWord(randomLetter, randomWord)
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print("Bien ! La lettre {0} fait partie du mot".format(str(randomLetter)))
            else:
                motion.say("Perdu ! La lettre {0} ne fait pas partie du mot".format(str(randomLetter)))
                print("Perdu ! La lettre {0} ne fait pas partie du mot".format(str(randomLetter)))
                hmGame.nbrRemainingChances -= 1

            motion.say("Il te reste {0} chances".format(str(hmGame.nbrRemainingChances)))
            print("Il te reste {0} chance(s)".format(str(hmGame.nbrRemainingChances)))


        #Fin de partie !
        if hmGame.didNaoLost():
            motion.say("Bravo ! Tu as reussi, le mot est {0} ".format(randomWord))
            print("Bravo ! Tu as reussi, le mot est {0} ".format(randomWord))
        if hmGame.didNaoWin() :
            motion.say("Oh ! Tu as perdu, le mot est {0} ".format(randomWord))
            print("Oh ! Tu as perdu, le mot est {0} ".format(randomWord))

    except BaseException as err:
        print(err)
    return randomWord



