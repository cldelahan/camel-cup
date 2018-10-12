import game
import sim

def getRecomendedMovement(g1):
    camels = ["Orange", "Yellow", "Green", "Blue", "White"]
    sim1 = sim.Sim(g1)
    # getting the maximum value from the simulations
    shortTermEV = sim1.simShortTerm()
    longTermEVW = sim1.simLongTerm()[0]
    longTermEVL = sim1.simLongTerm()[1]
    desertTileEV, tiles = sim1.simDesertTiles()
    maxST = max(shortTermEV)
    maxLTW = max(longTermEVW)
    maxLTL = max(longTermEVL)
    maxDT = max(desertTileEV)
    # printing recomendations
    if (maxST == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = shortTermEV.index(maxST)
        print ("Bet Short Term")
        print ("Camel: " + str(camels[index]) + " - " + str(index))
        print ("Expected Value: " + str(maxST))
    elif (maxDT == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = desertTileEV.index(maxDT)
        print ("Place Desert Tile")
        print ("Position: " + str(tiles[index]))
        print ("Expected Value: " + str(maxST))
    elif (maxLTW == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = longTermEVW.index(maxLTW)
        print ("Bet Long Term Winner")
        print ("Camel: " + str(camels[index]) + " - " + str(index))
        print ("Expected Value: " + str(maxLTW))
    elif (maxLTL == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = longTermEVL.index(maxLTL)
        print ("Bet Long Term Loser")
        print ("Camel: " + str(camels[index]) + " - " + str(index))
        print ("Expected Value: " + str(maxLTL))
    else:
        print ("Roll")
        print( "Expected Value: " + str(1.0))

def playGame(g1):
    # while there is no winner
    while (g1.board.checkWinner() == -1):
        print(g1)
        print("Recommended Options:")
        getRecomendedMovement(g1)
        print()
        print("Movement Options")
        print("1 - Roll\n2 - Bet Short-Term\n3 - Bet Long-Term\n4 - Place Backward DT\n5 - Place Forward DT")
        movement = int(input("Selection: "))
        if (movement == 1):
            diceNum = -1
            # making sure can move this color
            while (not(diceNum in g1.diceRemaining)):
                print("0-Orange, 1-Yellow, 2-Green, 3-Blue, 4-White")
                diceNum = int(input("Enter Color Number: "))
            value = -1
            # make sure rolling only 1 or 3
            while (value < 1 or value > 3):
                value = int(input("Enter Dice Value (1-3): "))
            g1.roll(diceNum, value)
            # if it is the end of a moment
            if (len(g1.diceRemaining) == 0):
                g1.resetDiceRem()
                g1.resetDesertTiles()
                g1.resetPayout()
        elif (movement == 2):
            colorNumber = -1
            # while the colorNumber is a valid dice and there is a short-term card to take
            while (colorNumber > 4 or colorNumber < 0 or g1.getSTPayout()[colorNumber] == 0):
                print("0-Orange, 1-Yellow, 2-Green, 3-Blue, 4-White")
                colorNumber = int(input("Enter Color Number: "))
            g1.betShort(colorNumber)
        elif (movement == 3):
            winLose = -1
            while (not (winLose == 0 or winLose == 1)):
                winLose = int(input("Enter Win(0) or Lose (1): "))
            g1.betLong(winLose)
        elif (movement == 4):
            pos = -1
            # while the position is in range and there is not already a Desert Tile or a camel at that square
            while (True):
                try:
                    pos = int(input("Enter position: "))
                    g1.placeBackwardTile(pos)
                    break
                except:
                    print("There is already a Desert Tile at this or an adjacent location")
                    # input showed some error
                    # g1.placeBackwardTile checks if tile are valid
        elif (movement == 5):
            pos = -1
             # while the position is in range and there is not already a Desert Tile or a camel at that square
            while (True):
                try:
                    pos = int(input("Enter position: "))
                    g1.placeForwardTile(pos)
                    break
                except:
                    print("There is already a Desert Tile at this or an adjacent location")
                    # input showed some error
                    # g1.placeBackwardTile checks if tile are valid
        else:
            print("Error: Operation invalid. Enter number 1-5")
        print()
        print()

        if (not(g1.board.checkWinner() == -1)):
            print("----------------")
            print("-----WINNER-----")
            print("---GAME OVER!---")
            print("----------------")
            break