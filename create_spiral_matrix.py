def create_spiral_matrix(arr, m, n):
    top = 0
    left = 0
    right = m - 1
    bottom = n - 1
    matrix = []
    for i in range(top, bottom + 1):
        matrix.append([])
        for j in range(left, right + 1):
            matrix[i].append(0)
    k = 0
    while k < len(arr):
        if left > right:
            return matrix
        for i in range(left, right + 1):
            matrix[top][i] = arr[k]
            k += 1
        top += 1
        if top > bottom:
            return matrix
        for i in range(top, bottom + 1):
            matrix[i][right] = arr[k]
            k += 1
        right -= 1
        if left > right:
            return matrix
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = arr[k]
            k += 1
        bottom -= 1
        if top > bottom:
            return matrix
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = arr[k]
            k += 1
        left += 1
    return matrix

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
m = 5
n = 5
print create_spiral_matrix(elements, m, n)
print create_spiral_matrix(elements, m, n) == [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
