def bubble_sort(arr)
  sorted = false
  swaps = 0
  i = 0
  until sorted == true
    while i < arr.length - 1
      if arr[i] > arr[i+1]
        arr[i], arr[i+1] = arr[i+1], arr[i]
        swaps += 1
      end
      i += 1
    end
    if swaps > 0
      swaps = 0
      i = 0
    elsif swaps == 0
      sorted = true
    end
  end
  arr
end

p bubble_sort([156,6,8,1,3,4,0,14])
