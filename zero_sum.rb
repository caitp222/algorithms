# brute force method
def zero_sum(arr)
  i = 0
  arrays = []
  while i < arr.length
    sum = 0
    w = i
    while w < arr.length
      sum += arr[w]
      if sum == 0
        arrays << arr[i..w]
      end
      w += 1
    end
    i += 1
  end
  arrays
end

arr1 = [4,2,-3,-1,0,4]
arr2 = [3,4,-7,3,1,3,1,-4,-2,-2]
p zero_sum(arr1)
p zero_sum(arr2)
