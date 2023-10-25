# Check if it is safe to insert `k` to the `board`
def safe(row,col,k,board): #function to check whether it is safe to insert a no. in board or not
    for i in range(9):
        if board[row][i]==k: # for checking element in same row
            return False
        if board[i][col]==k: # for checking element in same column
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3]==k: # for checking element in same box
            return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]=='.':
                for k in range(1,10):
                    k=str(k)
                    if safe(i,j,k,board):
                        board[i][j]=k
                        if solve(board):
                            return True
                        board[i][j]='.'
                return False # if it is not possible to insert any particular value at that cell
    return True # if all the values are filled then it will return True

r1 = list('685.3..1.')
r2 = list('...7.....')
r3 = list('47386...5')
r4 = list('..85....6')
r5 = list('.5.1.6.4.')
r6 = list('7.6..895.')
r7 = list('9...8.5.4')
r8 = list('8...52...')
r9 = list('.6..1..8.')
solve([r1, r2, r3, r4, r5, r6, r7, r8, r9])
print([r1, r2, r3, r4, r5, r6, r7, r8, r9])