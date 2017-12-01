# find longest increasing subsequence in a list
# find length of longest subsequence
def longest_increasing_sub_length(lst):
    longest_subsequence = 0
    longest_so_far = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            longest_so_far += 1
        else:
            if longest_subsequence < longest_so_far:
                longest_subsequence = longest_so_far + 1
            longest_so_far = 0
    return longest_subsequence

# returns the sequence itself, or first subsequence of max length
def longest_increasing_subsequence(lst):
    longest_subsequence = []
    longest_so_far = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            longest_so_far += 1
        else:
            if len(longest_subsequence) <= longest_so_far:
                longest_subsequence = lst[i - longest_so_far - 1:i]
            longest_so_far = 0
    return longest_subsequence


print longest_increasing_sub_length([3,2,6,4,5,1])
print longest_increasing_sub_length([2,10,6,14,1,9,5,13,3,4,5,9,11,7,15])

print longest_increasing_subsequence([3,2,6,4,5,1])
print longest_increasing_subsequence([2,10,6,14,1,9,5,13,3,4,5,9,11,7,15])
