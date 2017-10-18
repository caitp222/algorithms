def sort_binary(arr)
  count = 0
  i = 0
  while i < arr.length
    if arr[i] == 0
      count += 1
    end
    i += 1
  end
  array = []
  count.times do
    array << 0
  end
  (arr.length - count).times do
    array << 1
  end
  array
end

arr = [1,0,1,1,0,0,0,0,0,1,0]
p sort_binary(arr)
