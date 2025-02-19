import random
playerCards = []
cpuCards = []

playerstwos = 0
cputwos = 0

cardDeck = ["King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10]

random.shuffle(cardDeck)

name = input("Welcome, What Is You're Name, Fisherman?:")
print("Welcome To Go Fish",name,"!")

for x in range(7):
    card = cardDeck.pop()
    playerCards.append(card)
    print("The Cards That You Got Were:",playerCards)

for i in range(7):
    card = cardDeck.pop()
    cpuCards.append(card)














       
    

   






