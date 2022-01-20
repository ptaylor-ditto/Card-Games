import random, time, os

restart = "yes"

while restart.lower() == "yes":
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    p1cards = []
    p2cards = []
    p3cards = []
    p4cards = []
    deck = []
    played = []
    players = 4

    #creating the deck
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    
    random.shuffle(deck)

    #dealing the deck
    while len(deck) > 3:
        card = random.choice(deck)
        deck.remove(card)
        p1cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p2cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p3cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p4cards.append(card)

    deckstatus = ""

    while len(p1cards) > 0 and len(p2cards) > 0 and len(p3cards) > 0 and len(p4cards) > 0:

        #choosing the cards

        os.system('cls')
        print(p1cards)
        p1play = input("P1, choose your card.")
        if p1cards.count(p1play) >= 1:
            p1cards.remove(p1play)
            played.append(p1play)
        
        os.system('cls')
        print(p2cards)
        p2play = input("P2, choose your card.")
        if p2cards.count(p2play) >= 1:
            p2cards.remove(p2play)
            played.append(p2play)
        
        os.system('cls')
        print(p3cards)
        p3play = input("P3, choose your card.")
        if p3cards.count(p3play) >= 1:
            p3cards.remove(p3play)
            played.append(p3play)
        
        os.system('cls')
        print(p4cards)
        p4play = input("P4, choose your card.")
        if p4cards.count(p4play) >= 1:
            p4cards.remove(p4play)
            played.append(p4play)

        #finding numbers in cards
        p1number = p1play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p1number)
        p2number = p2play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p2number)
        p3number = p3play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p3number)
        p4number = p4play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p4number)
        played.remove(p1play)
        played.remove(p2play)
        played.remove(p3play)
        played.remove(p4play)

        #determines which is higher
        if p1number > p2number and p1number > p3number and p1number > p4number:
            p1cards.append(p1play)
            p1cards.append(p2play)
            p1cards.append(p3play)
            p1cards.append(p4play)
            print(f"Player 1, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.")

        elif p2number > p1number and p2number > p3number and p2number > p4number:
            p2cards.append(p1play)
            p2cards.append(p2play)
            p2cards.append(p3play)
            p2cards.append(p4play)
            print(f"Player 2, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.")

        elif p3number > p1number and p3number > p2number and p3number > p4number:
            p3cards.append(p1play)
            p3cards.append(p2play)
            p3cards.append(p3play)
            p3cards.append(p4play)
            print(f"Player 3, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.")

        elif p4number > p1number and p4number > p2number and p4number > p3number:
            p4cards.append(p1play)
            p4cards.append(p2play)
            p4cards.append(p3play)
            p4cards.append(p4play)
            print(f"Player 4, you won the battle. You gained the {p1play}, the {p2play}, the {p3play}, and the {p4play}.")

        else:
            p1cards.append(p1play)
            p2cards.append(p2play)
            p3cards.append(p3play)
            p4cards.append(p4play)
            print(f"There was a tie. The cards were returned to the decks.")
        
        os.system('cls')

    #Who won?
    if len(p1cards) == 0:
        print("Congratulations, Player 2. You won the Game of War.")

    if len(p2cards) == 0:
        print("Congratulations Player 1. You won the Game of War.")

    restart = input("Would you like to play again?")

#Saying goodbye... for now
print("You have finished the game.\nGoodbye.")