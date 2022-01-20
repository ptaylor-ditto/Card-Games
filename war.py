import random, time, os
from oneplayer import player1
from twoplayers import player2

restart = "yes"

while restart == "yes":
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    p1cards = []
    cpucards = []
    p2cards = []
    deck = []

    p2question = input("Are there one or two players? ")

    os.system('cls')

    if p2question.lower() == "1" or p2question.lower() == "one":
        print("Welcome to the Game of War. You are playing against a computer.")
        players = "1"

    if p2question == "2" or p2question == "two":
        print("Welcome to the Game of War.")
        players = "2"


    time.sleep(2)
    os.system('cls')

    #creating the deck
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')

    random.shuffle(deck)

    #dealing the deck
    
    deckstatus = ""

    if players == "1":
        while len(deck) > 1:
            card = random.choice(deck)
            deck.remove(card)
            p1cards.append(card)
            card = random.choice(deck)
            deck.remove(card)
            cpucards.append(card)
        player1(p1cards, cpucards, deckstatus, random, os, restart)

    if players == "2":
        while len(deck) > 1:
            card = random.choice(deck)
            deck.remove(card)
            p1cards.append(card)
            card = random.choice(deck)
            deck.remove(card)
            p2cards.append(card)
    if players == "2":
        player2(p1cards, p2cards, deckstatus, random, os, restart)

#Saying goodbye... for now
print("You have finished the game.\nGoodbye.")