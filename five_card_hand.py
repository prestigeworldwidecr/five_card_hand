## five_card_hand.py

## Write a function that takes 5 cards and return a string of what's the best possible hand. Determine if cards are in order and if cards are in the same suit.

## No jokers

## 1) create a function comparing two cards for rank
## 2) create function comparing suit
## function to determine IsRoyalFlush, IsStraightFlush, Is4ofaKind...
import math
import random
from collections import Counter

class Card:
    
    rank = None
    suit = None
    dealt = False
    index = None
    rankCount = 1
    suitCount = 1
    
    ## create new cards
    ## accept rank, suit
    def __init__ (self, r, s) :
        self.rank = ranks[r]
        self.suit = suits[s]
        # dealt = True    

    def print(self) :
        print(self.rank, " ", self.suit, " ", self.dealt, " ", self.index)

def createDeck() :
    # cnt = 0
    deck = []
    
    for i in range(0, 13) :
        for j in range (0, 4):
            deck.append(Card(i, j))
            # deck.append((Card(i, j))
            # randCard = 
            # print (randCard.rank, " ", randCard.suit)
            # print (deck [cnt].rank, deck [cnt].suit)
            # print (deck [cnt])
            # cnt = cnt + 1
            # print (i, " ", j)
            
    return deck



def dealRandomCard(deck) :
    # , 
    # print (deck [i].rank)
    # deck[i]
    # return
    # while (deck [i].dealt = True) :
    
    i = random.randint(0, 51)
    # cnt = 0
    # c = deck [i]
    # print ("**i1: ", i)
    
    if (deck [i].dealt == True) :
        # print ("**")
        
        while deck [i].dealt == True :
            i = random.randint(0, 51)
            
            # print ("**i2: ", i)
            # c = deck [i]
    
    # else :
    deck [i].dealt = True
    deck [i].index = i
    # cnt = cnt + 
    # return deck [i]
    return i
        
def dealHand(deck) :
    # c = None
    hand = []
    # print (len(d))
    
    for i in range(0, 5) :
        # c = dealCard(deck)
        # print(c.rank, " " , c.suit)
        hand.append(dealRandomCard(deck))
        # print (i)
    
    # print(len(hand))
    
    return hand
    
def isSameRank(card1, card2) :
    # sameRank = False
    return (card1.rank == card2.rank)
    
def isSameSuit(card1, card2) :
    # sameSuit = False
    return (card1.suit == card2.suit)
    
def highestCardFullDeck(deck) :
    # handIndices = []
    
    for i in range(51, -1, -1) :
        if (deck [i].dealt == True) :
            # handIndices.append(i)
            return deck [i]
            # print(i)
    # return handIndices

def printHand(deck, hand) :
    # handIndices = []
    
    for i in range(0, 5) :
        # print(deck [hand [i]].rank, " " , deck [hand [i]].suit, " ", deck [hand [i]].index, " ", deck [hand [i]].index, " ", deck [hand [i]].rankCount, " ", deck [hand [i]].suitCount)
        print(deck [hand [i]].rank, " " , deck [hand [i]].suit)
        # print(math.floor(deck [hand [i]].index / 4))
        # print (deck [hand [i]].rank)
        # print(deck [hand [i]].rank, " " , deck [hand [i]].suit)
        
def rank_suit_Count(deck, hand) :
    handSize = len(hand)
    
    # print (handSize)
    for i in range(handSize - 1, -1, -1) :
        # print 
        for j in range(handSize - 2, -1, -1) :
            # print (deck [hand [i]].print(), " " , deck [hand [j]].print())
            
            if (j == 0) :
                handSize = handSize - 1
                
            if (isSameRank(deck [hand [i]], deck [hand [j]])) :
                deck [hand [i]].rankCount = deck [hand [i]].rankCount + 1
                deck [hand [j]].rankCount = deck [hand [j]].rankCount + 1
                
            if (isSameSuit(deck [hand [i]], deck [hand [j]])) :
                deck [hand [i]].suitCount = deck [hand [i]].suitCount + 1
                deck [hand [j]].suitCount = deck [hand [j]].suitCount + 1
                
            # else :
                # print("hope not")
              # a = 1
            
                
        # deck [item].rankCount = deck [item].rankCount + 1
        # deck [item].suitCount = deck [item].suitCount + 1
        # print(deck [item].rank, " ", deck [item].suit, deck [item].rankCount)
    # sum (hand.rank == 
    # pass
    
def dealManualCard(deck, index) :
    deck [index].dealt = True
    deck [index].index = index

def generateTonyHand(deck, hand) :
    for item in hand :
        dealManualCard(deck, item)
        # print (item)
        # deck [hand [i]].dealt = True
        # print(deck [item].rank, " " , deck [item].suit, deck [item].index, deck [item].dealt)
    
def printDeck(deck) :    
    for i in range(0, 52) :
        deck [i].index = i
        print(deck [i].rank, " " , deck [i].suit, deck [i].index, deck [i].dealt)
        
def isFlush(deck, hand) :
    return (deck [hand [0]].suitCount == 5)
    
def isStraight(deck, hand) :
    for i in range(0, 4) :
        # print(math.floor(deck [hand [i]].index / 4) + 1, " ", math.floor(deck [hand [i + 1]].index / 4))
        if ((math.floor(deck [hand [i]].index / 4) + 1) != math.floor(deck [hand [i + 1]].index / 4)) :
            return False
            
    return True              

def highestCard(deck, hand) :
    return deck [hand [4]]
    # return deck [sortedTonyHand[4]]
    
def isFourKind(deck, hand) :
    return (deck [hand[0]].rankCount == 4 or deck [hand[0]].rankCount == 4)

def hasPair(deck, hand) :
    for i in range(0, 5) :
        # print(deck
        if (deck [hand [i]].rankCount == 2) :
            return True
            
    return False
    
def hasTwoPair(deck, hand) :
    twicePairCount = 0
    
    for i in range(0, 5) :
        # print(deck
        if (deck [hand [i]].rankCount == 2) :
            twicePairCount = twicePairCount + 1
            
    return (twicePairCount == 4)
            # i = i + 2       
            # if (deck [hand [i]].rankCount == 2) :
                # print(deck [hand [i]].rankCount
                # return True
            
    # return False
    
def hasTriple(deck, hand) :
    for i in range(0, 5) :
        # print(deck
        if (deck [hand [i]].rankCount == 3) :
            return True
            
    return False
    
def determineHand(deck, hand) :
    # handType = ""
    
    # check royal flush
    if (isStraight(deck, hand) and isFlush(deck, hand) and (highestCard(deck, hand).rank == 'A')) :
        return "royal flush"
        
    elif (isStraight(deck, hand) and isFlush(deck, hand)) :
        return "straight flush"
        
    elif (isFourKind(deck, hand)) :
        return "four of a kind"
        
    elif (hasTriple(deck, hand) and hasPair(deck, hand)) :
        return "full house"
        
    elif (isFlush(deck, hand)) :
        return "flush"
        
    elif (isStraight(deck, hand)) :
        return "straight"
        
    elif (hasTriple(deck, hand)) :
        return "three of a kind"
        
    elif (hasTwoPair(deck, hand)) :
        return "two pair"
        
    elif (hasPair(deck, hand)) :
        return "pair"
        
    else :
        return "high card: " + str(highestCard(deck, hand).rank) + " "+ highestCard(deck, hand).suit

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ["club", "spade", "heart", "diamond"]

# hand1 = [49, 33, 25, 16, 48]
# hand2 = [45, 41, 36, 34, 31]
# hand3 = [16, 12, 14, 15, 18]
# hand4 = [23, 20, 27, 24, 32]
# hand5 = [3, 7, 11, 28, 32]

d = createDeck()
# h = dealHand(d)
# hands = []
# [sorted(dealHand(d), sorted(dealHand(d), sorted(dealHand(d), sorted(dealHand(d), sorted(dealHand(d)]

for i in range(0, 10) :
    h = sorted(dealHand(d))
    rank_suit_Count(d, h)
    printHand(d, h)
    print(determineHand(d, h))
    # hands.append(h)



# sortedHand = sorted(h, key=lambda Card: Card.index)
# sortedHand = sorted(h)
# rank_suit_Count(d, h)
# printHand(d, sortedHand)
# print (determineHand(d, sortedHand))

# h1 = dealHand(d)
# sortedHand = sorted(h, key=lambda Card: Card.index)
# sortedHand1 = sorted(h1)
# rank_suit_Count(d, h1)
# print()
# printHand(d, sortedHand1)
# print (determineHand(d, sortedHand1))

# sortedTonyHand = sorted(hand5)
# generateTonyHand(d, sortedTonyHand)
# rank_suit_Count(d, sortedTonyHand)
# printHand(d, sortedTonyHand)
# print (determineHand(d, sortedTonyHand))

# print(hasTwoPair(d, sortedTonyHand))
# print(hasTriple(d, sortedTonyHand))
# print(hasPair(d, sortedTonyHand))

# print(isStraight(d, sortedTonyHand))
# print(isFlush(d))
# highestCard(d, sortedTonyHand).print()

# printDeck(d)
# h = dealHand(d)
# sortedHand = sorted(h, key=lambda Card: Card.index)
# printHand(sortedHand)

# print (len(h))
# print(len(d))
# print("highest card: ", highestCard(d).rank, highestCard(d).suit)
# printHand(h)
# print(sorted(h, key=lambda Card: Card.index) [0].print())
# printHand(sorted(h, key=lambda Card: Card.index))

# math.floor(()
# print (len(h))


# 2 0
# 3 1
# 4 2
# 5 3
# 6 4
# 7 5
# 8 6
# 9 7 
# 10 8
# J 9
# Q 10
# K 11
# A 12

# C 0
# S 1
# H 2
# D 3

# AS 10S 8S 6C AC (12, 2), (8, 1), (6, 0), (4, 0), (12, 0) (49, 33, 25, 16, 48)
# KS QS JC 10H 9D (11, 1), (10, 1), (9, 0), (10, 2), (7, 3) (45, 41, 36, 34, 31)
# 6C 5C 5H 5D 6H (4, 0), (3, 1), (3, 2), (3, 3), (4, 2) (16, 12, 14, 15, 18)
# 7D 7C 8D 8C 10C (5, 3), (5, 1), (6, 3), (6, 0), (8, 0) (23, 20, 27, 24, 32)
# 2D 3D 4D 9C 10C (0, 3), (1, 3), (2, 3), (7, 0), (8, 1) (3, 7, 11, 28, 32)

# ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# suits = ["club", "spade", "heart", "diamond"]

# print(h[2].print())
# print(len(h))

# for i in range(0, 52) :
  # print(d [i].rank, " " ,d [i].suit, " ",d [i].dealt)
    
# for i in range(0, 5) :
   # print(h [i].rank, " " ,h [i].suit, " ",h [i].dealt)

# a = isSameRank(d [0], d [4])
# print(isSameRank(d [0], d [3]))

# print(h[0].rank, " " , h[0].suit)

# print(len(h))

# firstCard = dealCard(d)

# print (firstCard.rank, " ", firstCard.suit)

# dealFirstCard

# print(len(d))


# r1 = random.randint(1,13)
# s1 = random.randint(1,4)

# firstCard = Card(r1, s1)
 
# print("Rank: ", r, "Suit: ", s) 
# print ("Rank: ", firstCard.rank, "Suit: ", firstCard.suit)


        