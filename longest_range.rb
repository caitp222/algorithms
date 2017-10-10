# Longest Range
# https://github.com/WomenWhoCodeNYC/Algorithms/blob/master/challenges/longestRange/longestRange.md

# first define a sort method
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
      sorted = false
      swaps = 0
      i = 0
    elsif swaps == 0
      sorted = true
    end
  end
  arr
end

# longest range method
def longest_range(arr)
  bubble_sort(arr)
  new_arr = []
  i = 0
  until i == arr.length
    if arr[i] - 1 == arr[i-1]
      new_arr << arr[i]
    end
    i += 1
  end
  new_arr
end

arr = [16, 6, 12, 5, 4, 10, 2, 11, 13, 3, 15]
p longest_range(arr)
