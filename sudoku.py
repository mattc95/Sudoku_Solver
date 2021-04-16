# -*- coding: utf-8 -*-
"""
Created on Thu Nov 5 01:42:06 2019

@author: matt
"""

#!/usr/bin/env python
# coding: utf-8

# expert
board = [[6,0,0,0,0,5,0,0,0],
         [0,0,0,3,0,9,0,5,0],
         [0,0,0,0,4,0,0,6,0],
         [4,0,3,0,0,0,0,0,0],
         [0,8,0,7,0,0,2,0,0],
         [0,0,0,0,0,1,7,0,0],
         [0,0,0,0,9,0,0,0,6],
         [0,0,5,0,2,0,8,4,9],
         [0,4,0,0,0,3,0,0,0]]

# check if inputing n at [x, y] is possible
def checkPossible(board, x, y, n):
    for i in range(9):
        if board[x][i]==n:
            return False
        
    for i in range(9):
        if board[i][y]==n:
            return False
        
    boxX = x // 3 * 3
    boxY = y // 3 * 3
        
    for i in range(3):
        for j in range(3):
            if board[boxX+i][boxY+j]==n:
                return False

    return True

# print the Board properly
def printBoard(board):
    for i in board:
        print(i)


# solve the input board by brute force
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1,10):
                    if checkPossible(board, i, j, n):
                        board[i][j] = n
                        solve(board)
                        board[i][j] = 0
                return
    print('final board: ')
    printBoard(board)

solve(board)
