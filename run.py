import game
import sim

g1 = game.Game([5, 2, 2, 2, 2], [0, 2, 1, 0, 3])

print(sim.Sim(g1).simShortTerm())
g1.placeBackwardTile(4)
g1.placeBackwardTile(3)
print(sim.Sim(g1).simShortTerm())
g1.resetDesertTiles()
print(sim.Sim(g1).simShortTerm())
g1.placeForwardTile(4)
print(sim.Sim(g1).simShortTerm())
g1.placeForwardTile(3)
print(sim.Sim(g1).simShortTerm())



