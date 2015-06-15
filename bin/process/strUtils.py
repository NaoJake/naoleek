__author__ = 'Justine Dewilde'

def getPositionOfLetterInWord(letter, word):
    "Retourne la liste des positions (0 a n) de la lettre dans le mot"
    i = 0
    result = []
    while i < len(word):
        if(word[i] == letter):
            result.append(i)
        i += 1

    return result