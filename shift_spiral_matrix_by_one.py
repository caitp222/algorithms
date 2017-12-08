def shift_spiral_matrix(arr):
    top = 0
    left = 0
    right = len(arr[0]) - 1
    bottom = len(arr) - 1
    prev = arr[top][left]
    while True:
        if left > right:
            break
        for i in range(left, right + 1):
            arr[top][i], prev = prev, arr[top][i]
        top += 1
        if top > bottom:
            break
        for i in range(top, bottom + 1):
            arr[i][right], prev = prev, arr[i][right]
        right -= 1
        if left > right:
            break
        for i in range(right, left - 1, -1):
            arr[bottom][i], prev = prev, arr[bottom][i]
        bottom -= 1
        if top > bottom:
            break
        for i in range(bottom, top - 1, -1):
            arr[i][left], prev = prev, arr[i][left]
        left += 1
    arr[0][0] = prev
    return arr


m = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
print shift_spiral_matrix(m) == [[25,1,2,3,4],[15,16,17,18,5],[14,23,24,19,6],[13,22,21,20,7],[12,11,10,9,8]]
