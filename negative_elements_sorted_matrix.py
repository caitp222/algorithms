# http://www.techiedelight.com/count-negative-elements-present-sorted-matrix/

def negative_count(arr):
    right = len(arr[0]) - 1
    top = 0
    negative_count = 0
    while right >= 0 and top < len(arr):
        if arr[top][right] < 0:
            negative_count += right + 1
            top += 1
        else:
            right -= 1
    return negative_count

m = [[-7,-3,-1,3,5],[-3,-2,2,4,6],[-1,1,3,5,8],[3,4,7,8,9]]
print negative_count(m)
