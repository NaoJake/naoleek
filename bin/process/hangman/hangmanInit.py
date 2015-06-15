import time
from bin.process.hangman import hangmanGame
from bin.process.naoUtils import naoLEDSOther, naoTalk, naoLEDSCorrect, naoLEDSError
from bin.process.strUtils import getPositionOfLetterInWord
from letter.Dispatcher import make_initial_dash, write_at_position

__author__ = 'Justine Dewilde'



def playGame(motionTalk, motionLED, motionProxy):
    "fonction permettant de lancer le jeu"

    try:
        welcome = "Bonjour, nous allons jouer au pendu ! Je vais d'abord choisir un mot"
        naoLEDSOther(motionLED)
        time.sleep(1)
        naoTalk(motionTalk, welcome)
        print(welcome)
        hmGame = hangmanGame.HangmanGame()
        randomWord = hmGame.getWordToFind()
        naoTalk(motionTalk, "Voila ! Ce mot a {0} lettres".format(str(len(randomWord))))
        naoTalk(motionTalk, "C'est parti !")
        print("Voila ! Ce mot a {0} lettres".format(str(len(randomWord))))
        print("C'est parti !")
        time.sleep(1)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #ajouter la partie permettant d'ecrire les traits : nbr de traits > (len(randomWord)
        make_initial_dash(len(randomWord), motionProxy)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(randomWord)

        #Partie
        while not(hmGame.didNaoLost()) and not(hmGame.didNaoWin()):
            randomLetter = ""
            while True :
                randomLetter = str(raw_input('Entrez une lettre: '))
                if(hmGame.lettersAlreadySay.count(randomLetter) == 0) :
                    break

            #randomLetter = hmGame.getRandomLetter()
            hmGame.putLetter(randomLetter)
            if hmGame.correctLetter(randomLetter):
                naoLEDSCorrect(motionLED)
                naoTalk(motionTalk, "Bien ! La lettre {0} fait partie du mot".format(str(randomLetter)))
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #fonction a mettre ici : nao ecrit la lettre : lettre > randomLetter & liste des positions :  getPositionOfLetterInWord(randomLetter, randomWord)
                positions = getPositionOfLetterInWord(randomLetter, randomWord)
                write_at_position(randomLetter, positions, motionProxy)
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print("Bien ! La lettre {0} fait partie du mot".format(str(randomLetter)))
            else:
                naoLEDSError(motionLED)
                naoTalk(motionTalk, "Perdu ! La lettre {0} ne fait pas partie du mot".format(str(randomLetter)))
                print("Perdu ! La lettre {0} ne fait pas partie du mot".format(str(randomLetter)))
                hmGame.nbrRemainingChances -= 1

            naoTalk(motionTalk, "Il te reste {0} chances".format(str(hmGame.nbrRemainingChances)))
            print("Il te reste {0} chance(s)".format(str(hmGame.nbrRemainingChances)))
            time.sleep(1)

        #Fin de partie !
        if hmGame.didNaoLost():
            naoTalk(motionTalk, "Bravo ! Tu as reussi, le mot est {0} ".format(randomWord))
            print("Bravo ! Tu as reussi, le mot est {0} ".format(randomWord))
        if hmGame.didNaoWin() :
            naoTalk(motionTalk, "Oh ! Tu as perdu, le mot est {0} ".format(randomWord))
            print("Oh ! Tu as perdu, le mot est {0} ".format(randomWord))

    except BaseException as err:
        print(err)
    return randomWord



