# Find the max number of consecutive ones in a binary array

def max_ones(arr)
  i = 0
  w = 0
  count = 0
  while i < arr.length
    if arr[i] == 1
      w += 1
    elsif  arr[i] == 0
      count = w
      w = 0
    end
    i += 1
  end
  if w > count
    count = w
  end
  count
end

arr = [1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1]
p max_ones(arr)
