import game
import play
        

print("------------------------------")
print("Welcome to Camel Cup Simulator")
print("---------Version 1.0----------")
print("------------------------------")
print()

numPlayers = input("Enter Number of Players: ")
print()

print("Orange, Yellow, Green, Blue, White")
org_pos, yel_pos, grn_pos, blu_pos, wht_pos = map(int, input("Enter initial positions: ").split(','))
org_tie, yel_tie, grn_tie, blu_tie, wht_tie = map(int, input("Enter initial tie values: ").split(','))
g1 = game.Game([org_pos, yel_pos, grn_pos, blu_pos, wht_pos], [org_tie, yel_tie, grn_tie, blu_tie, wht_tie])

print()
play.playGame(g1)