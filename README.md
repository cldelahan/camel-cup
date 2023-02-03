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



## Previous Summary from Website

Motive: Recently, I have become really interested in "solving" games - or rather - trying to design a strategy to play a certain game perfectly. This stems primarily from studying blackjack and card counting with friends, and has inspired to to try and solve Texas Hold'em. However, this is no easy feat, and en route, I have decided to "solve" a popular game that my family plays frequently

Project: Created a set of tools to mimic, simulate, and give advice for any game of Camel Cup

Tools: Python

Writeup:
To begin, Camel Cup is a game where players bet on camels that race around a board. Players of the game can choose to either bet on the camels' position after a "moment", bet on the long-term results of the race, place desert tiles on the board to affect the motion of the camels, or roll the pyramid, which causes any camel to move 1 to 3 spaces. As it seems, the game is very statistical and rooted deeply in probability. Rules
The project contains a few files that offers resources to virtually mimic the game and simulate future odds.

Representing the state of the board (board.py)
Representing the sate of the game, allowing for movement, winning, and computing first and last places (game.py)
Simulating a game in the future, with features such as calculating the estimated value of short-term betting, long-term betting, and the effects of placing desert tiles (sim.py)
Playing a game on the computer and being able to easily queue in the motions of players on the table in real life. (play.py)
Finally, a final run file that offers a game-side companion that gives the best move at any point in time. (run.py)
This then can be used alongside playing the game in real life to maximize money in the game, and thus win.
This project is currently completed, but there are future opportunities to create a mobile application version (because using a computer is kinda awkward). Additionally, we can study Camel Cup as whole, and if we assume that the application works perfectly, we can put computers against themselves and measure the effect of different variables in the game, notably turn position (going first or second etc.) or simply pure luck.

I really learned a lot from this project, most notably the difference between Deterministic Algorithms and Nondeterministic Algorithms. Originally, I had tried calculating every possibility and seeing which are favorable, but this route, although most accurate, would just take too much time. Rather, I looked into running a probabilistic test a few thousand times, and then looking at the results of that to make good approximations of the actual odds.

 

Current Status and Future Modifications:
(Issue: 10/15/17, Resolved: XX/XX/XX)

After playing many testing rounds, I discovered that Camel Cup was performing far poorer than it had in the past. After some consideration, I think I figured it out.

When playing, I looked at every movement as an attempt to maximize personal wealth. The logic was that maxmizing personal wealth would be the best route to winning. However, I frogot that to win, all you need is more money than the opponents, not as much money as possible. Thus, situations arise where it is best to take a $-2.00 sacrifice for yourself to harm the opponents $-5.00 instead of doing an option that would gain you $2.00.

Decisions of this sort only arise when choosing to place Desert Tiles. In placing them, you are not trying to get the small amounts of money that arise from camels potentially landing on the tile, but rather the comparative advantage over your oponents through thwarting their bets and enhancing your own bets.

Thus, in order to perform better, I need to have some sort of representation for each player playing the game (a player.py file), and record of which bets they have made and their money count. Then, I can create a modified estimated value that includes the harm given to other players. This could get tricky when deciding which players I should harm. For example, it is obviously best to harm the leading player the most because he / she is who I want to defeat, but what amount of harming players with less money than I have is equal to me simply progressing myself to beat top players.
