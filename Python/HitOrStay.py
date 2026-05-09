import random as rnd

active = True
cpuActive = False
victorious = False
player = rnd.randint(1,10)
cpu = rnd.randint(1,10)
game = 0

pWins = 0
cWins = 0
ties = 0

print(f"\n--------------------- ROUND {game+1} ---------------------\n")

while active == True:
    if(player != 21):
        pInput = input(f"---------------------\n{player}\n\n1 - Hit\n2 - Stay\n3 - End Game\n")
    else:
        pInput = "2"

    if(pInput == "1"):
        player += rnd.randint(1,10)
    elif(pInput == "2"):
        active = False
        print(f"---------------------\nStayed at {player}")

        cpuActive = True
        while cpuActive == True:
            if(cpu < 17):
                cpu += rnd.randint(1,10)
            else:
                cpuActive = False
        if(cpu > 21):
            victorious = True
        elif(cpu == player):
            active = False
            ties+=1
            input(f"\nYou: {player}\nCPU: {cpu}\n--------------------- TIE ---------------------")
            # restart game
            game+=1
            print(f"\n--------------------- ROUND {game+1} ---------------------\n")
            active = True
            cpuActive = False
            victorious = False
            player = rnd.randint(1,10)
            cpu = rnd.randint(1,10)
            active = True
        elif(cpu > player):
            active = False
            cWins+=1
            input(f"\nYou: {player}\nCPU: {cpu}\n--------------------- YOU LOST ---------------------")
            # restart game
            game+=1
            print(f"\n--------------------- ROUND {game+1} ---------------------\n")
            active = True
            cpuActive = False
            victorious = False
            player = rnd.randint(1,10)
            cpu = rnd.randint(1,10)
            active = True
        else:
            victorious = True

        if(victorious == True):
            active = False
            pWins+=1
            input(f"\nYou: {player}\nCPU: {cpu}\n--------------------- YOU WON ---------------------")
            # restart game
            game+=1
            print(f"\n--------------------- ROUND {game+1} ---------------------\n")
            active = True
            cpuActive = False
            victorious = False
            player = rnd.randint(1,10)
            cpu = rnd.randint(1,10)
            active = True
    elif(pInput == "3"):
        active = False
        print(f"--------------------- GAME HAS ENDED ---------------------\nRESULTS:\nMatches Played: {game}\nPlayer Wins: {pWins}\nCPU Wins: {cWins}\nTies: {ties}")
        if(pWins == 0 and cWins == 0 and ties == 0):
            print("\nWow, no competition? What a waste of time!\n")
        elif(pWins > cWins):
            print("\nCONGRATULATIONS, YOU ARE THE WINNER!\n")
        elif(pWins == cWins):
            print("\nIt's a tie!\n")
        else:
            print("\nBetter luck next time!\n")
    else:
        print("\nTHAT IS NOT AN OPTION")

    if(player > 21):
        active = False
        cWins+=1
        input(f"\n{player}\n--------------------- YOU LOST ---------------------")
        # restart game
        game+=1
        print(f"\n--------------------- ROUND {game+1} ---------------------\n")
        active = True
        cpuActive = False
        victorious = False
        player = rnd.randint(1,10)
        cpu = rnd.randint(1,10)
        active = True