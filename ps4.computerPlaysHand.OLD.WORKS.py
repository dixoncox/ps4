from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxWordScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = ''
    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
    for i in wordList:
        if isValidWord(i, hand, wordList):
            if getWordScore(i, n) > maxWordScore:
                maxWordScore = getWordScore(i, n)
                bestWord = i
    if bestWord != '':
        return bestWord
    else:
        return None


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function

    word = ''
    score = 0
    while (word != None) and (calculateHandlen(hand)>0):
        print 'Current Hand:',
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word != None:
            score += getWordScore(word,n)
            print '"'+word+'" earned', getWordScore(word, n),'points. Total:',score,'points'
            hand = updateHand(hand,word)
            print
    print 'Total score: ' + str(score) + ' points.'