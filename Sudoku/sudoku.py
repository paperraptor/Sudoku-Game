from random import seed
from random import randint
import random
import sys
#from pygame.locals import *
import pygame
import constant
from constant import *
import button
from button import *
import copy

class Sudoku:
    def __init__(self):
        self.grid = EMPTY_GRID
        self.answer = EMPTY_GRID
        self.empty = []
        self.isFilled = False
    
    def printGrid(self):
        for row in self.grid:
            print(row)
            
    def isNumValid(self, row, col):
        num = self.grid[row][col]
        #check row
        if self.grid[row].count(num) > 1:
            #print("no")
            return False
        #check colunm
        count = 0
        for i in range(9):
            if self.grid[i][col] == num and i != row:
                #print("no")
                return False
        #check group
        count = 0
        groupx = row - (row % 3)
        groupy = col - (col % 3)
        for x in range(groupx, groupx + 3):
            for y in range(col - (col % 3), col - (col % 3) + 3):
                if x != row and y != col and self.grid[x][y] == num:
                    return False
        return True
    
    def solveGrid(self, row, col, p):
        if row > 8:
            return True
        
        next_col = col+1
        next_row = row
        if col > 7:
            next_col = 0
            next_row += 1
        
        if self.grid[row][col] != 0:
            return self.solveGrid(next_row, next_col, p)
        
        poss = p[:] 
        num = 0
        
        while poss:
            num = random.choice(poss)  
            poss.remove(num)
            if len(poss) == 0:
                break
            self.grid[row][col] = num
            if self.isNumValid(row, col):
                if self.solveGrid(next_row, next_col, p):
                    return True
                
        self.grid[row][col] = 0

        return False
    
    def generateGrid(self):
        self.grid = EMPTY_GRID        
        poss = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
        self.solveGrid(0, 0, poss)
        #self.answer = self.grid.copy()
    
    def isSolvableHelper(self, row, col, num):
        if row > 8:
            return True
        
        next_col = col+1
        next_row = row
        if col > 7:
            next_col = 0
            next_row += 1
        
        if self.grid[row][col] != 0:
            self.grid[row][col] = 0
            return self.solveGrid(next_row, next_col, [1,2,3,4,5,6,7,8,9])
        

        self.grid[row][col] = num
        if self.isNumValid(row, col):
            if self.solveGrid(next_row, next_col, [1,2,3,4,5,6,7,8,9]):
                self.grid[row][col] = 0
                return True
                
        self.grid[row][col] = 0

        return False        
    
    def isSovable(self, row, col):
        count = 0
        for i in range(1, 9):
            if self.isSolvableHelper(row, col, i):
                count += 1
            if count > 1:
                return False
        if count == 0:
            return False
        else:
            return True
    
    def generateQuestion(self, numSpace):
        validSpace = []
        row = 0
        col = 0
        i = 0
        holder = 0
        while i < numSpace:
            row = randint(0,8)
            col = randint(0,8)
            
            if self.grid[row][col] != 0:
                holder = self.grid[row][col]
                self.grid[row][col] = 0
                if self.isSovable(row, col):
                    validSpace.append([row, col])
                    self.empty.append((row,col))
                    i += 1
                else:
                    self.grid[row][col] = holder
                    
            for coordinate in validSpace:
                self.grid[coordinate[0]][coordinate[1]] = 0
        
if __name__=="__main__":
    s = Sudoku()
    s.generateGrid()
    s.printGrid()