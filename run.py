import game
import sim

def getRecomendedMovement(g1):
    camels = ["Orange", "Yellow", "Green", "Blue", "White"]
    sim1 = sim.Sim(g1)
    shortTermEV = sim1.simShortTerm()
    longTermEVW = sim1.simLongTerm()[0]
    longTermEVL = sim1.simLongTerm()[1]
    desertTileEV, tiles = sim1.simDesertTiles()
    maxST = max(shortTermEV)
    maxLTW = max(longTermEVW)
    maxLTL = max(longTermEVL)
    maxDT = max(desertTileEV)
    if (maxST == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = shortTermEV.index(maxST)
        print ("Bet Short Term")
        print ("Camel: " + str(camels[index]))
        print ("Expected Value: " + str(maxST))
    elif (maxDT == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = desertTileEV.index(maxDT)
        print ("Place Desert Tile")
        print ("Position: " + str(tiles[index]))
        print ("Expected Value: " + str(maxST))
    elif (maxLTW == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = longTermEVW.index(maxLTW)
        print ("Bet Long Term Winner")
        print ("Camel: " + str(camels[index]))
        print ("Expected Value: " + str(maxLTW))
    elif (maxLTL == max(maxST, maxLTW, maxLTL, maxDT, 1.0)):
        index = longTermEVL.index(maxLTL)
        print ("Bet Long Term Loser")
        print ("Camel: " + str(camels[index]))
        print ("Expected Value: " + str(maxLTL))
    else:
        print ("Roll")
        print( "Expected Value: " + str(1.0))


print("------------------------------")
print("Welcome to Camel Cup Simulator")
print("---------Version 1.0----------")
print("------------------------------")

numPlayers = input("Enter Number of Players: ")

print("Orange, Yellow, Green, Blue, White")
org_pos, yel_pos, grn_pos, blu_pos, wht_pos = map(int, input("Enter initial positions: ").split(','))
org_tie, yel_tie, grn_tie, blu_tie, wht_tie = map(int, input("Enter initial tie values: ").split(','))
g1 = game.Game([org_pos, yel_pos, grn_pos, blu_pos, wht_pos], [org_tie, yel_tie, grn_tie, blu_tie, wht_tie])

getRecomendedMovement(g1)

#g1 = game.Game([5, 2, 2, 2, 2], [0, 2, 1, 0, 3])

#print(sim.Sim(g1).simShortTerm())
#g1.placeBackwardTile(4)
#g1.placeBackwardTile(3)
#print(sim.Sim(g1).simShortTerm())
#g1.resetDesertTiles()
#print(sim.Sim(g1).simShortTerm())
#g1.placeForwardTile(4)
#print(sim.Sim(g1).simShortTerm())
#g1.placeForwardTile(3)
#print(sim.Sim(g1).simShortTerm())