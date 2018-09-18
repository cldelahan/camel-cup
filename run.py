import game
import sim

g1 = game.Game([1, 2, 3, 2, 2], [0, 1, 0, 2, 0])
g1.betLong(0)
g1.diceRemaining = [1]
print(sim.Sim(g1).simShortTerm())





