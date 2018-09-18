# Board holds the state of the board
# and offers movement functions
import copy
import itertools

class Board:
    # orange, yellow, green, blue, white
    pos = [0, 0, 0, 0, 0] # position of the five camels
    tie = [0, 0, 0, 0, 0] # tie values for the five camels
    
    # constructor setting pos and tie
    def __init__(self, posParam, tieParam):
        self.pos = posParam
        self.tie = tieParam   
        
    def getPos(self):
        return copy.deepcopy(self.pos)
    
    def getTie(self):
        return copy.deepcopy(self.tie)
        
    # returns all pieces at a position from down to up
    def findPiecesAtPos(self, position):
        piecesAtPos = []
        for x in range (len(self.pos)): # looping through positions
            if (self.pos[x]==position):
                piecesAtPos.append(10*self.tie[x] + x) # appending a weighted value
        piecesAtPos.sort() # sorting the weighted value
        for x in range (len(piecesAtPos)):
            piecesAtPos[x] = piecesAtPos[x] % 10
        return piecesAtPos
    
    # moves pieces amount of steps
    def move(self, piece, amount):
        # get list of starting pieces that are moving
        movingList = self.getMovingList(piece)
        # get list of ending pieces
        finalPieces = self.findPiecesAtPos(self.pos[piece] + amount)
        for x in range (len(movingList)):
            self.pos[movingList[x]] = self.pos[movingList[x]] + amount
        self.pos[piece] = self.pos[piece] + amount
        if (len(finalPieces) == 0):
            for x in range (len(movingList)):
                self.tie[movingList[x]] = self.tie[movingList[x]] - self.tie[piece]
            self.tie[piece] = 0
        else:
            for x in range (len(movingList)):
                self.tie[movingList[x]] = self.tie[movingList[x]] + 1 + self.tie[finalPieces[-1]] - self.tie[piece]
            self.tie[piece] = self.tie[finalPieces[-1]] + 1    
    
    # given a piece, get the pieces that would move with it
    def getMovingList(self, piece):
        piece_pos = self.pos[piece]
        piece_tie = self.tie[piece]
        movingList = []
        for x in range (len(self.pos)):
            if (self.pos[x]==piece_pos and self.tie[x] > piece_tie):
                movingList.append(x)
        return movingList  
    
    # check if there is a winner and return the winner
    # if no winner, return -1
    def checkWinner(self):
        for x in range (len(self.pos)):
            if (self.pos[x]>16):
                posWinners = self.findPiecesAtPos(self.pos[x])
                for y in range (len(posWinners)):
                    if (self.tie[y] == len(posWinners)-1):
                        return y
                return x
        return -1
    
    # return camel in the lead
    def getLeader(self):
        maxPos = 0
        maxCamel = -1
        for x in range (len(self.pos)):
            if (self.pos[x] > maxPos):
                maxCamel = x
                maxPos = self.pos[x]
            elif (self.pos[x] == maxPos):
                if (self.tie[x] > self.tie[maxCamel]):
                    maxPos = self.pos[x]
                    maxCamel = x
        return maxCamel    
             
    # check for second place and return who is in second
    def getSecond(self):
        score = [0, 0, 0, 0, 0]
        for x in range (len(self.pos)):
            score[x] = self.pos[x]*10 + self.tie[x]  
        maxScore = 0
        maxScorePos = -1
        secScore = 0
        secScorePos = -1
        for x in range (len(score)):
            if ((score[x]) > maxScore):
                secScorePos = maxScorePos
                secScore = maxScore
                maxScore = score[x]
                maxScorePos = x
            elif (score[x] > secScore):
                secScorePos = x
                secScore =score[x]
        return secScorePos
    
    # return camel in last place
    def getLast(self):
        minPos = 100
        minCamel = -1
        for x in range (len(self.pos)):
            if (self.pos[x] < minPos):
                minCamel = x
                minPos = self.pos[x]
            elif (self.pos[x] == minPos):
                if (self.tie[x] < self.tie[minCamel]):
                    minPos = self.pos[x]
                    minCamel = x
        return minCamel    
    
    # tostring()
    def __str__(self):
        output = ""
        for x in range (len(self.pos)):
            output += str(self.pos[x]) + " "
        output += "\n"
        for x in range (len(self.tie)):
            output += str(self.tie[x]) + " "
        output += "\n"
        return output