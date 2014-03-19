def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    handRemaining = hand.copy()
    inHand = True
    
    for k in word:
        if (k in handRemaining) and (handRemaining[k] > 0):
            handRemaining[k] = handRemaining[k]-1
            inHand = inHand*True
        else:
            inHand = False
    if inHand and (word in wordList):
        return True
    else:
        return False


#word = 'rapture' #should be false
#hand = {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1} 
#wordList = ['rapture']
word = 'even' #should be false
hand = {'i': 1, 'n': 1, 'e': 1, 'l': 2, 'v': 2}
wordList = ['even']
print isValidWord(word, hand, wordList)