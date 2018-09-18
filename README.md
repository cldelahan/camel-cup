# camel-cup

Conner Delahanty

Summer, Fall 2018

This respository offers a set of solution algorithms in an board-side companion for the popular board game,
Camel-Cup. The game involves betting on camels as they race around the board. While very fun to play, the
game is almost purely statistical, and these codes hope to, in a sense, "solve" the game and calculate the
best move to play at any given game position.

Additionally:

board.py contains class Board that manages the location and movement of all pieces on the board

game.py contains class Game that holds a Board object along with the payout statuses and the number of dice remaining

sim.py contains class Sim that has two Games, simGame and backupGame as instance variables. Sim runs simulations on simGame and returns the results (non-deterministic tests for speed). Game backupGame allows multiple simulations to be run on a single Game.

- and finally -

run.py offers a game-side companion that utilizes the previous files to give the user the best move at any given point in the game.