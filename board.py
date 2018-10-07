# Board holds the state of the board
# and offers movement functions
import copy
import itertools

class Board:
    # orange, yellow, green, blue, white
    pos = [0, 0, 0, 0, 0] # position of the five camels
    tie = [0, 0, 0, 0, 0] # tie values for the five camels
    forwardTiles = []
    backwardTiles = []
    
    # constructor setting pos and tie
    def __init__(self, posParam, tieParam, fDT = [], bDT = []):
        self.pos = posParam
        self.tie = tieParam
        self.forwardTiles = copy.deepcopy(fDT)
        self.backwardTiles = copy.deepcopy(bDT)
        
    
    # get Position instance variable
    def getPos(self):
        return copy.deepcopy(self.pos)
    
    
    # get Tie instance variable
    def getTie(self):
        return copy.deepcopy(self.tie)
        
    def setForwardTiles(self, i):
        # the forward tile is not adjacent to another tile
        totalTiles = self.forwardTiles + self.backwardTiles
        if (not(i in self.pos) and not (i+1 in totalTiles) and not (i-1 in totalTiles) and not(i in totalTiles)):
            self.forwardTiles.append(i)
        else:
            raise IOError ("Cannot place Desert Tile at that position")
        
    def setBackwardTiles(self, i):
        # cannot place a backward tile adjacent to another tile
        totalTiles = self.forwardTiles + self.backwardTiles
        if (not(i in self.pos) and not (i+1 in totalTiles) and not (i-1 in totalTiles) and not (i in totalTiles)):
            self.backwardTiles.append(i)
        else:
            raise IOError ("Cannot place Desert Tile at that position")
        
    def getForwardTiles(self):
        return copy.deepcopy(self.forwardTiles)
    
    def getBackwardTiles(self):
        return copy.deepcopy(self.backwardTiles)
    
    def clearDesertTiles(self):
        self.backwardTiles = []
        self.forwardTiles = []
    
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
        
        # update position of moving pieces
        for x in range (len(movingList)):
            self.pos[movingList[x]] = self.pos[movingList[x]] + amount

        # if there are no pieces at the end
        if (len(finalPieces) == 0):
            for x in range (len(movingList)):
                self.tie[movingList[x]] = x
        # if there are pieces at the end
        else:
            # moving forwards
            if (amount > 0):
                for x in range (len(movingList)):
                    self.tie[movingList[x]] = self.tie[movingList[x]] + 1 + self.tie[finalPieces[-1]] - self.tie[piece]  
            # moving backwards
            elif (amount < 0):
                for x in range (len(finalPieces)):
                    self.tie[finalPieces[x]] += len(movingList)
                for x in range (len(movingList)):
                    self.tie[movingList[x]] = x 
                    
        # checking for pieces on desert tiles
        for i in range (len(self.forwardTiles)):
            # if the camels moved onto the forward tile
            if (self.forwardTiles[i] in self.pos):
                camelNumber = self.findPiecesAtPos(self.forwardTiles[i])[0]
                self.move(camelNumber, 1)
        
        for i in range (len(self.backwardTiles)):
            # if the camels moved onto the backward tile
            if (self.backwardTiles[i] in self.pos):
                camelNumber = self.findPiecesAtPos(self.backwardTiles[i])[0]
                self.move(camelNumber, -1)
    
    
    # given a piece, get all pieces that are moving (at its level or above)
    def getMovingList(self, piece):
        piece_pos = self.pos[piece]
        piece_tie = self.tie[piece]
        piecesAtPos = self.findPiecesAtPos(piece_pos)
        movingList = []
        for x in range(len(piecesAtPos)):
            # >= so the passed piece is part of the moving list.
            if (self.tie[piecesAtPos[x]] >= piece_tie):
                movingList.append(piecesAtPos[x])
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
        output = "Board\n"
        output += str(self.pos) + "\n"
        output += str(self.tie) + "\n"
        output += "\nForward DT: "
        output += str(self.forwardTiles)
        output += "\nBackward DT: "
        output += str(self.backwardTiles)
        output += "\n"      
        return output