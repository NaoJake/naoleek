import random
from data.alphabet import listLetter
from data.dictionary import dictionaryList

__author__ = 'Justine Dewilde'


class HangmanGame:
    lettersAlreadySay = []

    def __init__(self):
        self.wordToFind = self.getRandomWord()
        self.nbrRemainingChances = 10

    def putLetter(self, letter):
        self.lettersAlreadySay.append(letter)

    def isLetterInWord(self, letter):
        if letter in self.wordToFind :
            return True
        else :
            return False

    def getRandomWord(self):
        randomWord = random.choice(dictionaryList)
        return randomWord

    def getRandomLetter(self):
        while True :
            randomLetter = random.choice(listLetter)
            if(self.lettersAlreadySay.count(randomLetter) == 0):
                break

        return randomLetter

    #Si il NAO a reussi, car la personne n'a plus de chance
    def didNaoWin(self):
        if self.nbrRemainingChances == 0 :
            return True
        else :
            return False

    def didNaoLost(self):
        if():
            return True

    #Si la personne a trouve tous les mots
    def lettersAlreadySayContainsWordToFind(self):
        i = 0
        result = True
        while i < len(self.wordToFind):
            if(self.lettersAlreadySay.count(self.wordToFind[i]) == 0) :
                return False
            else :
                i += 1

        return result

    def getWordToFind(self):
        return self.wordToFind

    def correctLetter(self, letter):
        "retourne vrai si la lettre est contenue dans le mot a trouver"
        i = 0
        result = False
        while (i < len(self.wordToFind)) and not(result):
            if(self.wordToFind[i] == letter) :
                result = True
            else:
                i += 1

        return result

