import json
import random

class TicTacToeAI(object):
    
    goodMoves = {}
    badMoves = {}
    currentGame = {}
    
    result = False
    
    def fitData(self,goodMoves,badMoves):
        self.goodMoves = json.loads(goodMoves)
        self.badMoves = json.loads(badMoves)
        
        for keys in self.goodMoves.keys():
            
            self.goodMoves[keys] = set(self.goodMoves[keys])
        
        for keys in self.badMoves.keys():
            
            self.badMoves[keys] = set(self.badMoves[keys])
    
    
    def getMove(self,boardStatus,availableMovesMap):
        
        moves = list(self.goodMoves.get(boardStatus,set()))
        
        if(len(moves)):
            
            random.shuffle(moves)
            self.currentGame[boardStatus] = moves[0]
            return moves[0]
        
        else:
            
            moves = self.badMoves.get(boardStatus,set())
            
            for j in availableMovesMap.keys():
                
                if(not j in moves):
                    
                    self.currentGame[boardStatus] = j 
                    return j
                
            moves = list(availableMovesMap.keys())
            random.shuffle(moves)
            
            self.currentGame[boardStatus] = moves[0]
            
            return moves[0]
        
    def storeData(self,good,bad):
        
        for keys in good.keys():
            
            good[keys] = list(good[keys])
        
        for keys in bad.keys():
            
            bad[keys] = list(bad[keys])
        
        
        f = open("trainedYes.txt","w")
        f.write(json.dumps(good))
        f.close()
        
        f = open("trainedNo","w")
        f.write(json.dumps(bad))
        f.close()
        
    def trainOnData(self,result):
        
        if(result):
            
            for moves in self.currentGame.keys():
                
                if(self.goodMoves.get(moves,0)):
                    
                    self.goodMoves[moves].add(self.currentGame[moves])
                    
                else:
                    
                    self.goodMoves[moves] = {self.currentGame[moves]}
                    
        else:
            
            for moves in self.currentGame.keys():
                
                if(self.badMoves.get(moves,0)):
                    
                    self.badMoves[moves].add(self.currentGame[moves])
                    
                else:
                    
                    self.badMoves[moves] = {self.currentGame[moves]}
            
                    
        self.storeData(self.goodMoves,self.badMoves)
        self.currentGame = {}
                    
                    
                    
        
        
    
            
    