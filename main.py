global N
N = 5

def matricsboard(board):
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print() 

def checkqueensafe(board,row,col):
    for i in range(col): 
        if board[row][i] == 1: 
            return False
    
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
	    
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True

def checkqueens(board,col):
    if col >= N: 
        return True
    
    for row in range(N): 
  
        if checkSafePosition(board, row, col): 
	            
            board[row][col] = 1
            if checkQueen(board, col + 1) == True: 
                return True
            board[row][col] = 0
    return False

def s0lveNQ():
    board = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]
    
    if checkQueen(board, 0) == False: 
        print ("Solution does not exist") 
        return False
	  
    printMatrix(board) 
    return True
    
    

s0lveNQ()
