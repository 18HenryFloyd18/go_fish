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


while True:
    while(len(playerCards) > 1 or len(cpuCards) > 1):
    
        whatCard = input("What Card Would You Like?:")

        if whatCard in cpuCards:
           print("Nice!")
           print(f"DEBUG: COMPUTER HAND{compCard}")
           print(f"DEBUG:{whatCard}")
           compCard.pop(whatCard)
           playerCards.pop(whatCard)
           playerstwos = playertwos + 1
        else:
           print("Go Fish!")
           goFish = random.choice(cardDeck)
           print("You Drew A",goFish,"From The Deck")
           playerCards.append(goFish)
           print(playerCards)
           cardDeck.pop(goFish)