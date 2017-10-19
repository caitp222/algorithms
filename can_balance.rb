def can_balance(arr, mid=arr.length/2)
  if arr.length == 1
    return true
  elsif arr.length == 2
    if arr[0] == arr[1]
      return true
    end
  elsif sum_half(arr[0..mid]) == sum_half(arr[mid+1..arr.length-1])
    return true
  elsif sum_half(arr[0..mid]) > sum_half(arr[mid+1..arr.length-1])
    until mid == 0
      return true if sum_half(arr[0..mid]) == sum_half(arr[mid+1..arr.length-1])
      mid -= 1
    end
  else
    until mid == arr.length
      return true if sum_half(arr[0..mid]) == sum_half(arr[mid+1..arr.length-1])
      mid += 1
    end
  end
  false
end

def sum_half(arr)
  sum = 0
  i = 0
  while i < arr.length
    sum += arr[i]
    i += 1
  end
  sum
end

p can_balance([1, 1, 1, 2, 1]) == true
p can_balance([2, 1, 1, 2, 1]) == false
p can_balance([10, 10]) == true
