def print_diagonal(arr):
    for i in range(len(arr)):
        j = i
        k = 0
        diagonal_arr = []
        while j >= 0:
            diagonal_arr.append(arr[j][k])
            j -= 1
            k += 1
        print diagonal_arr
    for i in range(1, len(arr[0])):
        j = i
        k = len(arr) - 1
        diagonal_arr = []
        while k >= 0 and j < len(arr[0]):
            diagonal_arr.append(arr[j][k])
            j += 1
            k -= 1
        print diagonal_arr

m = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]
print_diagonal(m)
