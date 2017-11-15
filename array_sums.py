# given a sorted array of integers and an integer
# two sum
def two_sum(arr, n):
    ans = []
    for i in arr:
        for j in arr[i:]:
            if i + j == n:
                ans.append([i,j])
    return ans

# three sum
def three_sum(arr, n):
    i = 0
    j = len(arr) - 1
    ans = []
    while i < j:
        x = n - arr[j] - arr[i]
        stuff = x is not arr[j] and x is not arr[i] and x in arr
        if stuff:
            ans.append([arr[i], arr[j], x])
        i += 1
        j -= 1
    return ans

# all possible combinations
def all_subsets(arr, target, partial=[], ans=[]):
    s = sum(partial)
    if s == target:
        ans.append(partial)
    if s >= target:
        return
    for i in range(len(arr)):
        el = arr[i]
        remaining = arr[i+1:]
        all_subsets(remaining, target, partial + [el], ans)
    return ans

arr = [1,2,3,4,5,6,7,8,9,10]
num = 12
print(two_sum(arr, num))
print(three_sum(arr, num))
print(all_subsets(arr, num))
