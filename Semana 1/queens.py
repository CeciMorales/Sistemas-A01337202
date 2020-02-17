"""
Cecilia Morales Arriaga, A01337202

ENVIRONMENT'S CHARACTERIZATION

Each queen represents a rational agent because it perceives the environment 
(board and other queens) and acts to achieve the best results. In this 
case, to choose a cell, she has to check if there is no other queen in rows, 
columns, and diagonals.

I think this exercise is an example of a deterministic environment because 
the next state is determined by the current state and the agent´s actions. 
When queen A is placed in a certain cell, the board is updated. So, when 
the program is looking where to place queen B, it must checks the updated 
board and act according to the situation. This means, to place queen B
in cell N if it follows the rules or looking for another cell if there is 
an issue. This action will repeat itself until the seven queens are placed. 

:) 
"""

def printBoard(board):
  auxBoard = [[0]*8 for _ in range(8)]

  for i in range(8):
    for j in range(8):
      auxBoard[i][j] = board[8*i+j]
      print(auxBoard[i][j], end = ", ")
    print('\n')
  print('\n')


def checkHorizontal(board, index):
  counter = 0

  for i in range(index * 8, 8 * (index + 1) ):
    if (board[i] != 0):
      counter = counter + 1
    
  if (counter == 1):
    return True
  elif (counter > 1):
    return False


def checkVertical(board, index):
  counter = 0

  for i in range(0, 8):
    if(board[index + i * 8] != 0 ):
      counter = counter + 1
  
  if (counter == 1):
    return True
  elif (counter > 1):
    return False


def checkDiagIzquierda(board, index):
  Realrow = -1
  Realcol = -1

  for i in range(8):  
    if (index > -1):
      row = index//8
      col = index%8

      if(row == 0 or col == 0):
        Realrow = row
        Realcol = col
        index = -1

      index = index - 9

  counter = 0
  num = Realrow * 8 + Realcol

  for j in range(8):
    if(num>=0):
      if (board[num] != 0):
        counter = counter + 1

      if (num//8 == 7 or num%8 == 7):
        num = -100

      num = num + 9

  if (counter == 1):
    return True
  elif (counter > 1):
    return False

def checkDiagDerecha(board, index):
  Realrow = -1
  Realcol = -1

  for i in range(8):
    if (index > -1):
      row = index//8
      col = index%8

      if(row == 0 or col == 7):
        Realrow = row
        Realcol = col
        index = -1
    
      index = index - 7

  counter = 0
  num = Realrow * 8 + Realcol

  for j in range(8):
    if(num>=0):
      if (board[num] != 0):
        counter = counter + 1

      if (num//8 == 7 or num%8 == 0):
        num = -100

      num = num + 7

  if (counter == 1):
    return True
  elif (counter > 1):
    return False

def checkRules(board, index):
  horizontal = checkHorizontal(board, index//8)
  vertical = checkVertical(board, index%8)
  diagDerecha = checkDiagDerecha(board, index)
  diagIzquierda = checkDiagIzquierda(board, index)

  if(horizontal and vertical and diagDerecha and diagIzquierda):
    return True
  else:
    return False

def placeQueen(board, col, queens):
  if (queens == 8):
    return board

  for i in range(8):
    index = i * 8 + col
    board[index] = 1
    
    if (checkRules(board, index) == True):
      done = placeQueen(board, col + 1, queens +1)
      if(done):
        return done

      board[index] = 0
          
    elif (checkRules(board, index) == False):
      board[index] = 0

def startGame(board):
  place = placeQueen(board, 0, 0)

board = [0]*64
startGame(board)
printBoard(board)