import random
import TicTacToeAI
import json

class TicTacToe(object):
    
    #board = " "*9
    board = [" "] * 9 #All the data is stored in string format
    playedBoxes = {} #Keys are int and values doesn't matter as long as it's not null or False values.
    unplayedBoxes = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1} #Keys are int and values doesn't matter as long as it's not null or False values.
    count = 9
    AI = None
    playerTurn = True
    
    def reset(self):
        
        self.board = [" "] * 9
        self.playedBoxes = {}
        self.unplayedBoxes = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
        self.AI = TicTacToeAI.TicTacToeAI()
        self.count = 9
        
    
    def __init__(self,playerTurn=True) -> None:
        
        self.playerTurn = playerTurn
        self.board = [" "] * 9
        self.playedBoxes = {}
        self.unplayedBoxes = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
        self.AI = TicTacToeAI.TicTacToeAI()
        
        f = open("trainedYes","r")
        goodMoves = f.read()
        f.close()
        f = open("trainedNo","r")
        badMoves = f.read()
        f.close()
        self.AI.fitData(goodMoves,badMoves)
        
    def startTraining(self,result):
        
        self.AI.trainOnData(result)
        
    
    def printBoard(self):
        
        print(" Board Status")
        print()
        print(self.board[0],"|",self.board[1],"|",self.board[2])
        print()
        print(self.board[3],"|",self.board[4],"|",self.board[5])
        print()
        print(self.board[6],"|",self.board[7],"|",self.board[8])
        print()
        print()
        
    def playerMove(self):
        
        move = int(input("Please enter your move 1 to 9 : "))
        
        while(move>9 or move<1 or self.playedBoxes.get(move,0)):
            
            print("Wrong Input Please Try Again.")
            move = int(input("Please enter your move 1 to 9 : "))
            
        self.playedBoxes[move] = 1
        self.board[move-1] = "O" if self.playerTurn else "X"
        del self.unplayedBoxes[move]
        self.count-=1

    
    def aiMove(self):
        
        move = self.AI.getMove("".join(self.board),self.unplayedBoxes)
        self.playedBoxes[move] = 1
        self.board[move-1] = "X" if self.playerTurn else "O"
        del self.unplayedBoxes[move]
        self.count-=1
    
    def checkWinner(self):
        
        if(self.board[0] == self.board[1] == self.board[2] != " "):
            
            return self.board[0]
        
        if(self.board[3] == self.board[4] == self.board[5] != " "):
            
            return self.board[3]
        
        if(self.board[6] == self.board[7] == self.board[8] != " "):
            
            return self.board[6]
        
        if(self.board[0] == self.board[3] == self.board[6] != " "):
            
            return self.board[0]
        
        if(self.board[1] == self.board[4] == self.board[7] != " "):
            
            return self.board[1]
        
        if(self.board[2] == self.board[5] == self.board[8] != " "):
            
            return self.board[2]
        
        if(self.board[0] == self.board[4] == self.board[8] != " "):
            
            return self.board[0]
        
        if(self.board[2] == self.board[4] == self.board[6] != " "):
            
            return self.board[2]
        
        if(self.count == 0):
            
            return "Draw"
        
        return False





game = TicTacToe()
game.printBoard()

while(True):
    
    try:
    
        game.playerMove() if game.playerTurn else game.aiMove()
        game.printBoard()
        result = game.checkWinner()
        if(result and result!="Draw"):
            print("Winner is : ",result)
            game.startTraining(False)
            break
        
        if(result=="Draw"):
            print("Draw")
            break
        
        game.aiMove() if game.playerTurn else game.playerMove()
        game.printBoard()
        result = game.checkWinner()
        if(result and result!="Draw"):
            print("Winner is : ",result)
            game.startTraining(True)
            break
        
    except:
        
        print("Exception Occurred : Restarting The Game ")
        game = TicTacToe()
        game.printBoard()
        
        