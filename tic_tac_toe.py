import random

# print the game board
def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' )
    print('- - - - - -')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' )
    print('- - - - - -')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' )

# take user input
def playerInput(board, current_player):
    global inp
    inp = int(input ('Enter number 1-9(Enter 0 for exit): '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = current_player
    else:
        print('Invalid input')

# check for win or tie
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

def checkTIE(board):
    if '-' not in board:
        global gameRunning
        printBoard(board)
        print('TIE')
        gameRunning = False

# switching players
def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'

def checkwin(board):
    global gameRunning
    if checkDiag(board) or checkVertical(board) or checkhorizontal(board):
        printBoard(board)  # Print the final board state
        print(f' The winner is {winner}')
        gameRunning = False

def computer(board, current_player):
    while current_player == 'O':
        pos = random.randint(0,8)
        if board[pos] == '-':
            board[pos] = 'O'
            return switch_player(current_player)
    return current_player

def main():
    global winner, gameRunning
    
    board = ['-','-','-',
             '-','-','-',
             '-','-','-']
    
    current_player = 'X'
    winner = None
    gameRunning = True
    
    while gameRunning:
        printBoard(board)
        playerInput(board, current_player)
        checkwin(board)
        checkTIE(board)
        current_player = switch_player(current_player)
        
        current_player = computer(board, current_player)
        if gameRunning:  # Only check for win if game is still running
            checkwin(board)
            checkTIE(board)

if __name__ == "__main__":
    main()