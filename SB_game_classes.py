import random
import networkx as nx
import math
from abc import ABC, abstractmethod

class TicTacOhNoException(Exception):
    "Raised when character selection is incorrect"
    pass

class InvalidBoardState(Exception):
    "Raised on the following: "
    "Turn player did not input a character that got printed!"
    "Turn player input invalid character!"
    "Box was occupado!"
    pass

class game(ABC):
    def getBoard(self, board):
        pass
    def getUnit(self, player):
        pass
    def getTurn(self):
        pass
    def printBoard(self):
        pass
    def getBoard(board):
        pass
    def getPlayer(player):
        pass
    def getTurn(self):
        pass
    def CreatePlayer(self):
        pass    
    def NextTurn(self, unit):
        pass
    def PlaceUnit(board):
        pass
    def isWin(self, board, unit):
        pass
    def isDraw(self):
        pass
    def GameEnd(self):
        pass

class Algorithm(ABC):
    def BestMove(self):
        pass
    def PlaceUnit(self):
        pass
    def isWin(self):
        pass
    def isDraw(self):
        pass


class tictactoe:
    empty = ' '
    circle = 'O'
    cross = 'X'
    width = 3
    height = 3
    playerCount = 2
    turn = cross
    lastTurn = circle
    def __init__(self, width=3,height=3):
        self.width = width
        self.height = height
        # self.board = gameBoard
        # self.playerCross = playerCross
        # self.playerCircle = playerCircle
        
    def getTurn(self):
        return self.turn
    
    def NextTurn(self, unit):
#        unit = player.getUnits()
        self.turn = unit
        self.lastTurn
        if unit == 'X':
            self.turn = 'O'
            self.lastTurn = 'X'
        elif unit == 'O':
            self.turn = 'X'
            self.lastTurn = 'O'
        return self.turn

    def isWin(self, board, unit=turn):
        boardSq = board.getGrid()
        if (boardSq[(1,1)]==boardSq[(1,2)] and boardSq[(1,1)]==boardSq[(1,3)] and boardSq[(1,1)] ==unit):
            return True
        elif (boardSq[(2,1)]==boardSq[(2,2)] and boardSq[(2,2)]==boardSq[(2,3)] and boardSq[(2,1)] ==unit):
            return True
        elif (boardSq[(3,1)]==boardSq[(3,2)] and boardSq[(3,1)]==boardSq[(3,3)] and boardSq[(3,1)] ==unit):
            return True
        elif (boardSq[(1,1)]==boardSq[(2,2)] and boardSq[(1,1)]==boardSq[(3,3)] and boardSq[(1,1)] ==unit):
            return True
        elif (boardSq[(1,3)]==boardSq[(2,2)] and boardSq[(1,3)]==boardSq[(3,1)] and boardSq[(1,3)] ==unit):
            return True
        elif (boardSq[(1,1)]==boardSq[(2,1)] and boardSq[(1,1)]==boardSq[(3,1)] and boardSq[(1,1)] ==unit):
            return True
        elif (boardSq[(1,2)]==boardSq[(2,2)] and boardSq[(1,2)]==boardSq[(3,2)] and boardSq[(1,2)] ==unit):
            return True
        elif (boardSq[(1,3)]==boardSq[(2,3)] and boardSq[(1,3)]==boardSq[(3,3)] and boardSq[(1,3)] ==unit):
            return True
        else:
            return False

    def isDraw(self, board):
        for key in board.gridSquare.keys():
            if (board.gridSquare[key]==' '):
                return False
        return True

    def GameEnd(self, board):
        if self.isWin(board, self.turn) or self.isDraw(board) or self.isWin(board, self.lastTurn):
            print(f"The game has ended!")
            if self.isWin(board, self.turn):
                print(f"The winner is {self.turn}!")
            elif self.isWin(board, self.lastTurn):
                print(f"The winner is {self.lastTurn}!")
            elif self.isDraw(self.turn):
                print("It's a draw!")
            self.turn = self.cross
            return True
        else:
            return False

class board(game):
    gridSquare = {}
    width = 3
    height = 3
    size = 9
    def __init__(self, game):
        self.width = game.width
        self.height = game.height
        self.size = self.width*self.height
        self.CreateGrid(self.width, self.height)

    def getGrid(self):
        return self.gridSquare
    
    def CreateGrid(self, width, height):
        for y in range(height):
            for x in range(width):
                self.gridSquare.update({(x+1, y+1): ' '})
        return self.gridSquare

    def printBoard(self):
        print(f"{self.gridSquare[(1,1)]} | {self.gridSquare[(1,2)]} | {self.gridSquare[(1,3)]}")
        print(f"{self.gridSquare[(2,1)]} | {self.gridSquare[(2,2)]} | {self.gridSquare[(2,3)]}")
        print(f"{self.gridSquare[(3,1)]} | {self.gridSquare[(3,2)]} | {self.gridSquare[(3,3)]}")

    def PlaceUnit(self, game, x, y):
        try:
            if self.width >= x > 0 and self.height >= y > 0:
                turn = game.getTurn()
                if self.gridSquare[(x,y)] == ' ':
                    self.gridSquare[(x,y)] = turn
                    if game.GameEnd(self):
                        print("That's all folks!")
                    else:
                        placed_unit = game.NextTurn(turn)
                        if placed_unit != turn:
                            return placed_unit
                        else:
                            print("Error swapping turns after placing unit!")
            else:
                raise TicTacOhNoException
        except TicTacOhNoException:
            print("Not a valid square!") 

    def emptyGrid(self):
        self.gridSquare = self.CreateGrid(self.width, self.height)
        return self.gridSquare

class player(game):
    unit = ' '
    def __init__(self, unit):
        self.unit = unit
    def getUnits(self):
        return self.unit
    # def AddUnit(self, unitName):
    #     self.unit.Append(unitName)

ttt = tictactoe()
gameBoard = board(ttt)
playerCross = player(ttt.cross)
playerCircle = player(ttt.circle)
#TTTBoard = board(newTTT.width, newTTT.height)


        
# Test Cases
x = 4
y = 4
turn = ttt.turn
print(f"It is {turn}'s turn to place a unit!") 
gameBoard.PlaceUnit(ttt, x, y) #Test 1, OOR
print(f"It is {turn}'s turn to place a unit!") #Test 2, turn swap on invalid moves
gameEnded = ttt.GameEnd(gameBoard)
for i in range(1,4): # Test 3, Case for turn swapping
    for j in range(1,4):
        if gameEnded == False: #Test Case 4, winner evaluation
            turn = gameBoard.PlaceUnit(ttt,i,j)
            print(f"It is {turn}'s turn to place a unit!")
            print(f"There is a {gameBoard.gridSquare[(i,j)]} at location {(i,j)}")
            gameEnded = ttt.GameEnd(gameBoard)
        else:
             print(f"Else, game has ended: {ttt.GameEnd(gameBoard)}")
             print(f"Unit at {(i,j)} is a {gameBoard.gridSquare[(i,j)]}")
             print()


gameBoard.printBoard()
#print(f"There is a {TTTBoard.gridSquare[(x,y)]} at location {TTTBoard.gridSquare.key((x,y))}")


"""""""""
Run Game
"""""""""
# while not ttt.GameEnd(gameBoard):
#     print(f"{ttt.getTurn()}")
#     print(f"{gameBoard}")
#     if(gameBoard.GameEnd(gameBoard) == False):
#         turn = ttt.getTurn()
#         gameBoard.PlaceUnit(turn, int(input(f"Place {turn} in Row: ")), int(input(f"Place {turn} in Column: ")))
#     elif(gameBoard.GameEnd() == False):
#         turn = ttt.getTurn()
#         gameBoard.PlaceUnit(turn, int(input(f"Place {turn} in Row: ")), int(input(f"Place {turn} in Column: ")))
#     if(ttt.GameEnd(gameBoard) == True):
#         print("Game Finished!")




