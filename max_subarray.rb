# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# greedy solution
def max_subarray(arr)
  i = 0
  max_sum = arr[i]
  until i == arr.length
    running_total = arr[i]
    w = i
    until w == arr.length
      running_total += arr[w]
      if max_sum && running_total > max_sum
        max_sum = running_total
        max_subarray = arr[i..w]
      end
      w += 1
    end
    i += 1
    running_total = 0
  end
  max_subarray
end

arr = [-2,1,-3,4,-1,2,1,-5,4]
# max subarray is [4,-1,2,1] which has the largest sum of 6
p max_subarray(arr)
