board = [
            [7,8,0,4,0,0,1,2,0],# 0
            [6,0,0,0,7,5,0,0,9],# 1
            [0,0,0,6,0,1,0,7,8],# 2
            [0,0,7,0,4,0,2,6,0],# 3
            [0,0,1,0,5,0,9,3,0],# 4
            [9,0,4,0,6,0,0,0,5],# 5
            [0,7,0,3,0,0,0,1,2],# 6
            [1,2,0,0,0,7,4,0,0],# 7
            [0,4,9,2,0,6,0,0,7] # 8
            #0 1 2 3 4 5 6 7 8       
                                        ]   

def print_board(board):
    # print ---- after every 3rd row only 
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print('-------------------')
        # print every number in the current row
        # add | after every 3rd number 
        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0:
                print('|', end='')
            
            if column == 8:
                print(str(board[row][column]))
            else:
                print(str(board[row][column]) + ' ', end='')

def find_empty(board):
    # loop to every row in the board
    for row in range(len(board[0])):
        # loop to every column in a row
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)
    
    return None

def check_board(board, number, position):
    # check horizontal/row
    for column in range(len(board[0])):
        if board[position[0]][column] == number and position[1] != column:
            return False            
    # check vertical/column
    for row in range(len(board)):
        if board[row][position[1]] == number and position[0] != row: 
            return False
    # check box
    box_x = position[1] // 3 # column is x 
    box_y = position[0] // 3 # row is y

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True
    
def solve(board):
    # get the position of empty
    empty = find_empty(board)
    # if there's no more empty then the board is already solved
    if not empty:
        return True
    else:
        # pass the position of empty 
        row, column = empty
    
    # insert values from 1 to 9 to the empty position 
    for number in range(1, 10):
        # if the number being inserted will be true when the board is checked, then add it to that position
        if check_board(board, number, (row, column)):
            board[row][column] = number

            # recursive function
            # find another empty spot and then fill it
            # if the solve function is true, then the board is solved
            if solve(board):
                return True

            # if not, then set the current position to 0 and then repeat again
            board[row][column] = 0 
    
    return False

#-----------------  
print('UNSOLVED\n')
print_board(board)          
solve(board)
solve(board)
print(' ')
print('SOLVED\n')
print_board(board)
