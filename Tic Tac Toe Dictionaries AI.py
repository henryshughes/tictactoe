import random
import time 

board = {'top-L':' ', 'top-M': ' ', 'top-R':' ', 'middle-L':' ', 'middle-M': ' ', 'middle-R':' ', 'bottom-L':' ', 'bottom-M': ' ', 'bottom-R':' '}
turn_list = []
combinations = [['top-L', 'top-M', 'top-R'], ['middle-L', 'middle-M', 'middle-R'], ['bottom-L', 'bottom-M', 'bottom-R'], ['top-L', 'middle-L', 'bottom-L'],
                ['top-M', 'middle-M', 'bottom-M'], ['top-R', 'middle-R', 'bottom-R'], ['top-L', 'middle-M', 'bottom-R'], ['top-R', 'middle-M', 'bottom-R']]
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['middle-L'] + '|' + board['middle-M'] + '|' + board['middle-R'])
    print('-+-+-')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R'])

def block(board, combinations):
    check = False
    for k in range(len(combinations)):
        count = 0
        for j in range(len(combinations[k])):
            if board[combinations[k][j]] == 'O':
                count +=1
            if board[combinations[k][j]] == 'X':
                count -=1
            if count == 2:
                check = True
                break 
        else:
            continue
        break
    return k, j, check

def win(board, combinations):
    check = False
    for k in range(len(combinations)):
        count = 0
        for j in range(len(combinations[k])):
            if board[combinations[k][j]] == 'O':
                count -=1
            if board[combinations[k][j]] == 'X':
                count +=1
            if count == 2:
                check = True
                break 
        else:
            continue
        break
    return k, j, check    
            
def computerTurn(board, combinations):
    print('It is the computer\'s turn')
    if turn_list == []:
        board['bottom-L'] = 'X'
    elif board['top-R'] == ' ' and len(turn_list) <=1 :
        board['top-R'] = 'X'
    elif board['bottom-R'] == ' ' and len(turn_list) <=1 :
        board['bottom-R'] = 'X' 
    elif len(turn_list) >= 2:
        k, j, check = block(board, combinations)
        a, z, check_two = win(board, combinations)
        if check_two:
            for r in range(len(combinations[a])):
                if board[combinations[a][r]] == ' ':
                    board[combinations[a][r]] = 'X'              
        elif check:
            for w in range(len(combinations[k])):
                if board[combinations[k][w]] == ' ':
                    board[combinations[k][w]] = 'X'                
def personTurn(board):
    print('It is your turn')
    space = input()
    board[space] = 'O' 
    turn_list.append(space)


turn = 'Computer'
for i in range(9):
    
    if i%2 == 0:
        computerTurn(board, combinations)
    else:
        personTurn(board)
    printBoard(board)
    if board['top-L'] == board['top-M'] and board['top-L'] == board['top-R']  and board['top-R'] == board['top-M'] and board['top-L'] != ' ':
        print(turn + " team has won the game")
        break
    elif board['middle-L'] == board['middle-M'] and board['middle-M'] == board['middle-R'] and board['middle-L'] == board['middle-R'] and board['middle-L'] != ' ':
        break       
    elif board['bottom-L'] == board['bottom-M'] and board['bottom-L'] == board['bottom-R'] and board['bottom-R'] == board['bottom-M'] and board['bottom-L'] != ' ':
        print(turn + " team has won the game")
        break  
    elif board['top-L'] == board['middle-L'] and board['bottom-L'] == board['middle-L'] and board['bottom-L'] == board['top-L'] and board['top-L'] != ' ':
        print(turn + " team has won the game")
        break       
    elif board['top-R'] == board['middle-R'] and board['bottom-R'] == board['middle-R'] and board['bottom-R'] == board['top-R'] and board['top-R'] != ' ':
        print(turn + " team has won the game") 
        break
    elif board['top-M'] == board['middle-M'] and board['bottom-M'] == board['middle-M'] and board['bottom-M'] == board['top-M'] and board['top-M'] != ' ':
        print(turn + " team has won the game")
        break
    elif board['top-L'] == board['middle-M'] and board['bottom-R'] == board['middle-M'] and board['top-L'] == board['bottom-R'] and board['top-L'] != ' ':
        print(turn + " team has won the game")    
        break
    elif board['top-R'] == board['middle-M'] and board['bottom-L'] == board['middle-M'] and board['top-R'] == board['bottom-L'] and board['top-R'] != ' ':
        print(turn + " team has won the game")   
        break
    if turn =='Computer':
        turn = 'Your'
    else:
        turn = 'Computer'
    
    if i == 8:
        print('Game was a tie')
        break    
    
    