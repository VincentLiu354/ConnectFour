# shell_connectfour.py
# Project 2: Send Me On My Way
#
# This module is program one of a two-program project involving the classic game connect four.
# The module allows a user to play connect four through the shell and with another player,
# also incorporating the pop variation of the game. 



# Importing starter module and libraries
from connectfour import *
from collections import namedtuple
from shared_functions import *

def startGame() -> None:
    ''' This function prints out the starting board, with the user input's columns and rows'''
    try:
        columnsInput = int(input('Enter the column size: '))
        rowsInput = int(input('Enter the row size: '))
    except:
        print('Invalid Input, please try again')
        startGame()
    
    newGame = (new_game(columnsInput, rowsInput))

    printBoard(newGame)


def runGame(newGame: GameState) -> None:
    ''' 
    This function asks the users if they want to drop or pop a piece
     Contains sub-functions that prompts the user to make a move based
     on their first decision, and if the move is invalid, prompts them again.
    '''
    print('Follow the format (DROP/POP) + (column #)')
    print('Example: DROP 4')
    userFirstMove = (input("Make your move: "))
    action = userFirstMove.split(' ')[0]
    number = int(userFirstMove.split(' ')[1])

    while True:
            try:
                if(action == 'DROP'):
                        printBoard(drop(newGame, number-1))
                        break
                elif(action == 'POP'):
                        printBoard(pop(newGame, number-1))
                        break
                else:
                        print('Invalid Move, please try again')
                        runGame(newGame)
            except:
                if(winner(newGame) == 1 or winner(newGame) == 2):
                    break
                print('Invalid Move, please try again')
                runGame(newGame)

def printBoard(newGame: GameState) -> None:
    '''
    Prints out the board and labeled column numbers, continuously does so
    after each move until a winner is determined, in which the program ends.
    '''

    for x in range(1, columns(newGame) + 1):
        if x >= 10:
            print("",x, end=" ")
        else:
            print(" ", x, end=" ")
   
    newGameRows = newGame.board[0] # [0,0,0,0,0]
    newGameColumns = newGame.board # [[0,0,0,0,0], [0,0,0,0,0], ...]

    try:
        if((len(newGameColumns) > len(newGameRows)) or (len(newGameColumns) == len(newGameRows))):
            for r in range(len(newGameColumns)):
                print('\n')
                for x in newGameColumns:
                    move = x[r]
                    if(move == 1):
                        print("  R", end=' ')
                    elif(move == 2):
                        print('  Y', end=' ')
                    elif(move == 0):
                        print('  .', end=' ')
                print()
        elif(len(newGameRows) > len(newGameColumns)):
            for r in range(len(newGameRows)):
                print('\n')
                for x in newGameColumns:
                    move = x[r]
                    if(move == 1):
                        print("  R", end=' ')
                    elif(move == 2):
                        print('  Y', end=' ')
                    elif(move == 0):
                        print('  .', end=' ')
                print()
    except:
        pass
    
    if(winner(newGame) == 1):
        print("Red Won!!!")
    elif(winner(newGame) == 2):
        print("Yellow Won!!!")
    else:
        print('\n', getTurn(newGame))
        runGame(newGame)

def getTurn(newGame: GameState) -> str:
    '''
    Assigns the turn number into a string that indicates
    which color's turn it is and returns it.
    '''
    turn = ''
    if(newGame.turn == 1):
        turn = "Red's Turn"
    elif(newGame.turn%2 == 0):
        turn = "Yellow's Turn"
    elif(newGame.turn%2 == 1):
        turn = "Red's Turn"

    return turn


if __name__ == '__main__':
    '''
    Ensures module only runs when executed, thus importing
    won't yield any other effects.
    '''
    startGame()

