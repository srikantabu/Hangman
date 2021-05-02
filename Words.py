"""Function to fetch words"""

import random

WORDLIST = 'wordlist.txt'

def getRandomWord(minWordLength):
    """Get a random word from the wordlist using no extra memory."""
    numWordsProcessed = 0
    currWord = None
    with open(WORDLIST,'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < minWordLength:
                continue
            numWordsProcessed += 1
            if random.randint(1, numWordsProcessed) == 1:
                currWord = word
    return currWord
