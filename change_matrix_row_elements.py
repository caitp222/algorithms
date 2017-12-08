# http://www.techiedelight.com/change-elements-row-column-j-matrix-0-cell-j-value-0/
# Given a matrix m x n consisting of only 0 or 1, change all elements of a row i and a column j to 0
# if cell (i,j) has value 0. Do this without using any extra space for every i,j having value 0.

def convert(arr):
    m = len(arr[0])
    n = len(arr)
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                arr[i][0] = 0
                arr[0][j] = 0
    for i in range(1, m):
        if arr[0][i] == 0:
            for j in range(n):
                arr[j][i] = 0
    for i in range(n):
        if arr[i][0] == 0:
            for j in range(m):
                arr[i][j] = 0
    if arr[0][0] == 0:
        for j in range(n):
            arr[j][0] = 0
    return arr

m = [[1,1,0,1,1],[1,1,1,1,1],[1,1,1,0,1],[1,1,1,1,1],[0,1,1,1,1]]
print convert(m) == [[0,0,0,0,0],[0,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,0,0,0,0]]
