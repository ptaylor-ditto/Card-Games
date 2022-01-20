def player1(p1cards, cpucards, deckstatus, random, os, restart):
    while len(p1cards) > 0 and len(cpucards) > 0:

        #ending the game at any time
        if deckstatus == "end":
            restart = "no"
            break

        #battle cards
        p1play = random.choice(p1cards)
        p1cards.remove(p1play)
        cpuplay = random.choice(cpucards)
        cpucards.remove(cpuplay)

        #finding numbers in cards
        p1number = p1play.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(p1number)

        cpunumber = cpuplay.translate({ord(i): None for i in 'abdefilmnoprstuCDHS'})
        print(cpunumber)

        #determines which is higher
        if p1number > cpunumber:
            p1cards.append(p1play)
            p1cards.append(cpuplay)
            print(f"You won the battle. You gained the the {p1play} and the {cpuplay}.")
            deckstatus = input("Do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p1cards)
                input("Press Enter to continue:")

        elif cpunumber > p1number:
            cpucards.append(p1play)
            cpucards.append(cpuplay)
            print(f"The computer won the battle. They gained the {p1play} and the {cpuplay}.")
            deckstatus = input("Do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p1cards)
                input("Press Enter to continue:")

        else:
            p1cards.append(p1play)
            cpucards.append(cpuplay)
            print(f"There was a tie between the {p1play} and the {cpuplay}. The cards were returned to the decks.")
            deckstatus = input("Do you want to see your deck right now? ")

            if deckstatus == "yes":
                os.system('cls')
                print(p1cards)
                input("Press Enter to continue:")
        
        os.system('cls')

    #Who won?
    if len(p1cards) == 0:
        print("I'm sorry, but the computer won this game of war.")

    if len(cpucards) == 0:
        print("Congratulations. You won the game of war.")