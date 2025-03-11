import random
playerCards = []
cpuCards = []

playerstwos = 0
cputwos = 0

cardDeck = ["King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10,"King","Queen","Ace","Joker","Jack",1,2,3,4,5,6,7,8,9,10]

def checkHands(card,hand):
    if card in hand:
        return 1
    else:
        return 0

random.shuffle(cardDeck)
name = input("Welcome, What Is You're Name, Fisherman?:")
print("Welcome To Go Fish",name,"!")



for x in range(7):
    card = cardDeck.pop()
    if checkHands(card,playerCards) > 0:
        # Code to increment the number of cards of that type
        playerstwos += 1
    playerCards.append(card)
print("The Cards That You Got Were:",playerCards)    

for i in range(7):
    card = cardDeck.pop()
    if checkHands(card,cpuCards) > 0:
        cputwos += 1
    cpuCards.append(card)


while True:
    while(len(playerCards) > 1 or len(cpuCards) > 1):
    
        whatCard = input("What Card Would You Like?:")

        if whatCard in cpuCards:
           print("Nice!")
           cpuCards.remove(whatCard)
           playerCards.remove(whatCard)
           playerstwos += 1
           print("You Now Have",playerstwos,"Duplicates In Your Hand")
           print("Computer Books:",cputwos)
           print("Your Cards:",playerCards)
        else:
            print("Go Fish!")
            goFish = random.choice(cardDeck)
            if goFish in playerCards:
                # Code that checks if the card is a duplicate and increases the count
                playerstwos += 1
            print("You Drew A",goFish,"From The Deck")
            playerCards.append(goFish)
            print(playerCards)
            cardDeck.remove(goFish)


        cpuGuess = random.choice(cpuCards)

        if cpuGuess in playerCards:
            print("The Computer Got A Book From Guessing")
            cpuCards.remove(cpuGuess)
            playerCards.remove(cpuGuess)
            cputwos += 1
            print("Computer Books",cputwos)
            print("Your Books:",playerstwos)
            print("Your Cards",playerCards)

        else:
            print("The Computer Has To Go Fishing")
            if cpuGuess in cpuCards:
                cputwos += 1
            cpuFishing = random.choice(cardDeck)
            cardDeck.remove(cpuFishing)
            cpuCards.append(cpuFishing)



    break