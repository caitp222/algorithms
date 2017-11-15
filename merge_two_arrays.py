# http://www.techiedelight.com/merge-two-arrays-satisfying-given-constraints/

def merge_two_arrays(arr1, arr2):
    x = 0
    for i in range(0, len(arr1)):
        if arr1[i] is 0:
            if i is len(arr1) - 1 or arr2[x] <= arr1[i + 1]:
                arr1[i] = arr2[x]
            elif arr2[x] > arr1[i + 1]:
                for w in range(i, len(arr1) - 1):
                    if arr2[x] <= arr1[w]:
                        break
                    else:
                        arr1[w], arr1[w + 1] = arr1[w + 1], arr1[w]
                arr1[w] = arr2[x]
            x += 1
    return arr1


arr1 = [0,2,0,3,0,5,6,0,0]
arr2 = [1,8,9,10,15]
print(merge_two_arrays(arr1, arr2) == [1,2,3,5,6,8,9,10,15])
