def player2(p1cards, p2cards, deckstatus, random, os, restart):
    while len(p1cards) > 0 and len(p2cards) > 0:

        #ending the game at any time
        if deckstatus == "end":
            restart = "no"
            break

        #battle cards
        p1play = random.choice(p1cards)
        p1cards.remove(p1play)
        p2play = random.choice(p2cards)
        p2cards.remove(p2play)

        #finding numbers in cards
        p1number = p1play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p1number)

        p2number = p2play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p2number)

        #determines which is higher
        if p1number > p2number:
            p1cards.append(p1play)
            p1cards.append(p2play)
            print(f"You won the battle. You gained the the {p1play} and the {p2play}.")
            deckstatus = input("Player 1, do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p1cards)
                input("Press Enter to continue:")
                
            deckstatus = input("Player 2, do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p2cards)
                input("Press Enter to continue:")

        elif p2number > p1number:
            p2cards.append(p1play)
            p2cards.append(p2play)
            print(f"The computer won the battle. They gained the {p1play} and the {p2play}.")
            deckstatus = input("Player 1, do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p1cards)
                input("Press Enter to continue:")
                
            deckstatus = input("Player 2, do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p2cards)
                input("Press Enter to continue:")

        else:
            p1cards.append(p1play)
            p2cards.append(p2play)
            print(f"There was a tie between the {p1play} and the {p2play}. The cards were returned to the decks.")
            deckstatus = input("Player 1, do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p1cards)
                input("Press Enter to continue:")
                
            deckstatus = input("Player 2, do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p2cards)
                input("Press Enter to continue:")
        
        os.system('cls')

    #Who won?
    if len(p1cards) == 0:
        print("Congratulations, Player 2. You won the Game of War.")

    if len(p2cards) == 0:
        print("Congratulations Player 1. You won the Game of War.")

    return p1cards, p2cards, deckstatus, restart