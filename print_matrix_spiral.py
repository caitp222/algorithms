def print_spiral_matrix_iterative(arr):
    top = 0
    left = 0
    right = len(arr[0]) - 1
    bottom = len(arr) - 1
    while True:
        if left > right:
            return
        for i in range(left, right + 1):
            print arr[top][i]
        top += 1
        if top > bottom:
            return
        for i in range(top, bottom + 1):
            print arr[i][right]
        right -= 1
        if left > right:
            return
        for i in range(right, left - 1, -1):
            print arr[bottom][i]
        bottom -= 1
        if top > bottom:
            return
        for i in range(bottom, top - 1, -1):
            print arr[i][left]
        left += 1

def print_spiral_matrix_recursive(arr, top=0, left=0, right=None, bottom=None):
    if right == None:
        right = len(arr[top]) - 1
    if bottom == None:
        bottom = len(arr) - 1
    if left > right:
        return
    for i in range(left, right + 1):
        print arr[top][i]
    top += 1
    if top > bottom:
        return
    for i in range(top, bottom + 1):
        print arr[i][right]
    right -= 1
    if left > right:
        return
    for i in range(right, left - 1, -1):
        print arr[bottom][i]
    bottom -= 1
    if top > bottom:
        return
    for i in range(bottom, top - 1, -1):
        print arr[i][left]
    left += 1
    print_spiral_matrix_recursive(arr, top, left, right, bottom)


m = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
print_spiral_matrix_iterative(m)
print_spiral_matrix_recursive(m)
