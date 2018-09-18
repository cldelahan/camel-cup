# Sim holds a deepcopy of a game as an instance variable and
# simulates best moves
import game
import random


class Sim:
    def __init__(self, initGame):
        self.backupGame = self.deepCopy(initGame) # copy of backup game to revert to
        self.simGame = self.deepCopy(initGame) # "liquid" game showing changes
        
    def deepCopy(self, g1):
        boardCopy = g1.copyBoard()
        boardPos = boardCopy.getPos()
        boardTie = boardCopy.getTie()
        diceRemaining = g1.getDiceRem()
        stPayout = g1.getSTPayout()
        ltPayout = g1.getLTPayout()
        return game.Game(boardPos, boardTie, diceRemaining, stPayout, ltPayout)

    def resetGame(self):
        self.simGame = self.deepCopy(self.backupGame)
    
    def randRoll(self): # roll a dice of diceRemaining randomly
        diceRem = self.simGame.getDiceRem()
        randomDice = diceRem[random.randrange(0, len(diceRem))]
        randomValue = random.randrange(1, 4)
        self.simGame.roll(randomDice, randomValue)
    
    # simulate the game numSims times
    def simLongTerm(self, numSims = 10000):
        timesFirst = [0, 0, 0, 0, 0]
        timesLast = [0, 0, 0, 0, 0]
        totalCompletedSimulations = 0
        # iterate through the number of Simulations
        for i in range (numSims):
            gameBoard = self.simGame.board
            self.randRoll()
            if (len(self.simGame.getDiceRem()) == 0):
                self.simGame.resetDiceRem()
            if (gameBoard.checkWinner() != -1):
                # incrementing the wins
                timesFirst[gameBoard.getLeader()] = timesFirst[gameBoard.getLeader()] + 1
                timesLast[gameBoard.getLast()] = timesLast[gameBoard.getLast()] + 1
                self.resetGame()
                totalCompletedSimulations += 1
        self.resetGame()
        
        if (totalCompletedSimulations == 0):
            totalCompletedSimulations = 1
        firstPercent = []
        lastPercent = []        
        for i in range (len (timesFirst)):
            firstPercent.append(round(timesFirst[i] / totalCompletedSimulations, 3))
            lastPercent.append(round(timesLast[i] / totalCompletedSimulations, 3))
        
        evWin = []
        evLose = []
        winLTPayout = self.simGame.getLTPayout()[0]
        loseLTPayout = self.simGame.getLTPayout()[1]
        for i in range (len(firstPercent)):
            # odds of winning * payout - odds of not winning * loss - lossed opportunity to bet on losing long-term
            evWin.append(round(firstPercent[i] * winLTPayout - (1 - firstPercent[i]) * 1 - (lastPercent[i] * loseLTPayout), 3))
            evLose.append(round(lastPercent[i] * loseLTPayout - (1 - lastPercent[i]) * 1 - (firstPercent[i] * winLTPayout), 3))
        # firstPercent, evWin, lastPercent, evLose
        return evWin, evLose   
    
    def simShortTerm(self, numSims = 10000):
        timesFirst = [0, 0, 0, 0, 0]
        timesSecond = [0, 0, 0, 0, 0]        
        totalCompletedSimulations = 0
        for i in range(numSims):
            gameBoard = self.simGame.board
            # roll until there are no more die (moment over)
            while(len(self.simGame.diceRemaining) != 0):
                self.randRoll()
            # increment timesFirst and timesSecond
            timesFirst[gameBoard.getLeader()] = timesFirst[gameBoard.getLeader()] + 1
            timesSecond[gameBoard.getSecond()] = timesSecond[gameBoard.getSecond()] + 1
            self.resetGame() # reset the game
            totalCompletedSimulations += 1
        self.resetGame()  
        
        if (totalCompletedSimulations == 0):
            totalCompletedSimulations = 1
            
        firstPercent = []
        secondPercent = []        
        for i in range (len (timesFirst)):
            firstPercent.append(round(timesFirst[i] / totalCompletedSimulations, 3))
            secondPercent.append(round(timesSecond[i] / totalCompletedSimulations, 3))  
        
        ev = [0, 0, 0, 0, 0]
        for x in range (len(firstPercent)):
            # ev is odds first * payout + odds second * 1 - not first or second * 1
            ev[x] = round(firstPercent[x] * self.simGame.getSTPayout()[x] + secondPercent[x] * 1 - (( 1 - firstPercent[x] - secondPercent[x]) * 1), 3)
        
        return ev
    
    def __str__(self):
        return self.simGame.__str__()
