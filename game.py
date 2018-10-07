# Defining Game Class
# Game is the overarching methods with simulating a game
import board
import copy

class Game:
    
    def __init__(self, posParam, tieParam, fDT = [], bDT = [], drParam = [0, 1, 2, 3, 4], stParam = [5, 5, 5, 5, 5], ltParam = [8, 8]):
        self.board = board.Board(posParam, tieParam, fDT, bDT) # the board for the game
        self.diceRemaining = drParam # the dice remaining in the pyramid
        self.stPayout = stParam # the short term stPayout remaining in each game moment
        self.ltPayout = ltParam # long term stPayout, separated in long-term win and long-term lose

    def copyBoard(self):
        pos = self.board.getPos()
        tie = self.board.getTie()
        fDT = self.board.getForwardTiles()
        bDT = self.board.getBackwardTiles()
        return board.Board(pos, tie, fDT, bDT)

    def getDiceRem(self):
        return copy.deepcopy(self.diceRemaining)
    
    def getSTPayout(self):
        return copy.deepcopy(self.stPayout)
    
    def getLTPayout(self):
        return copy.deepcopy(self.ltPayout)
        
    def resetDiceRem(self):
        self.diceRemaining = [0, 1, 2, 3, 4]
        
    def resetDesertTiles(self):
        self.board.clearDesertTiles()
        
    def removeDie(self, die):
        self.diceRemaining.pop(self.diceRemaining.index(die))
        
    def resetPayout(self):
        self.stPayout = [5, 5, 5, 5, 5]
        
    def roll(self, diceNum, value):
        assert(value < 4 and value > 0)
        self.board.move(diceNum, value)
        # removes the remaining dice
        self.removeDie(diceNum) 
        # if there are no more dice
        
    def betShort(self, color):
        if (self.stPayout[color] == 5):
            self.stPayout[color] = 3
        elif (self.stPayout[color] == 3):
            self.stPayout[color] = 2
        elif (self.stPayout[color] == 2):
            self.stPayout[color] = 0
            
    def betLong(self, winOrLose):
        # 0 is win, 1 is lose
        if (self.ltPayout[winOrLose] == 8):
            self.ltPayout[winOrLose] = 5
        elif (self.ltPayout[winOrLose] == 5):
            self.ltPayout[winOrLose] = 3
        elif (self.ltPayout[winOrLose] == 3):
            self.ltPayout[winOrLose] = 2
        elif (self.ltPayout[winOrLose] == 2):
            self.ltPayout[winOrLose] = 1   
            
    def placeBackwardTile(self, i):
        self.board.setBackwardTiles(i)

    def placeForwardTile(self, i):
        self.board.setForwardTiles(i)
    
    def __str__(self):
        output = ""
        output += self.board.__str__()
        output += "Dice Remaining: "
        output += str(self.diceRemaining)
        output += "\nST Payout: "
        output += str(self.stPayout)
        output += "\nLT Payout: "
        output += str(self.ltPayout)        
        output += "\n"
        return output
