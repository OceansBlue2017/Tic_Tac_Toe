                    # Tic Tac Toe game in Python

# This line is to create the board to store the X & O for the game.
# start with ' ' to give a leading space. 
board = [' ' for x in range(10) ] # using Ten, to get the user to enter numbers from 1 to 9

def inserLetter(letter, pos):  # this is to insert the letter into the board.
    board[pos] == letter

def spaceIsFree(pos):   # to check if the space is free or not before inserting the letter.
    return board[pos] == ' '   # == will give us if it is true or false value.

# to print the board to be used for the X, O game
def printBaord (board):
    print('  |  |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board [3])
    print('  |  |')
    print('----------')
    print('  |  |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board [6])
    print('  |  |')
    print('----------')
    print('  |  |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board [9])
    print('  |  |')
    print('----------')
    print('  |  |')
    
def isWinner (bo, le):  # bo stands for Board
    return (bo [7] == le and bo[8] == le and bo[9] == le) or
           (bo [4] == le and bo[5] == le and bo[6] == le) or
           (bo [1] == le and bo[2] == le and bo[3] == le) or
           (bo [1] == le and bo[4] == le and bo[7] == le) or
           (bo [2] == le and bo[5] == le and bo[8] == le) or
           (bo [3] == le and bo[6] == le and bo[9] == le) or
           (bo [1] == le and bo[5] == le and bo[9] == le) or
           (bo [3] == le and bo[5] == le and bo[7] == le) 


def playerMove ():
    run = True
    while run:
        move = input ('Please select a position to place an \'X\' (1-9):')
        try:
            move = int(move)
            if move > 0 and move < 10:  # to make sure user has inout between 1 & 9
                if spaceIsFree (move):
                    run = False
                    insertLetter ('X', move)
                else:
                    print ('Sorry this space is occupied!')
            else:
                print ('Please type a number within the range!')

        except:
            print('Please type a number! ') # in case user does not type an integer


def compMove ():
    pass

def selectRandom (board):
    pass

def isBoardFull (board):
    if board.count (' ') > 1:
        return True
    else
        return False


def main ():
    print (' Welcome to Tic Tac Toe game')
    prntBoard ()

    while not (isBaordFull (board) ): # if the board is full tie the game, no need to continue
        if not (isWinner (board, 'O') ): # check if the computer is the winner
            playerMove () 
            printBoard ()
        else:
            print ("sorry, O\'s won this round!")
            break

        if not (isWinner (board, 'X') ): # check if the computer is the winner
            compMove () 
            printBoard ()
        else:
            print (" X\'s won this round! Great Job!")
            break

    if isBoardFull (board):
        print ('Tie Game!')


main ()