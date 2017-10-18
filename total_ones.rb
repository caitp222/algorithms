# find number of 1s in a sorted binary array

# recursive solution
def total_ones(arr, low=0, high=arr.length-1)
  if arr[high] == 0
    return 0
  elsif arr[low] == 1
    return arr[low..arr.length-1].length
  end
  mid = (low + high)/2
  if arr[mid] == 0
    total_ones(arr, (mid+1), high)
  else
    total_ones(arr, low, mid)
  end

end

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
p total_ones(arr)
