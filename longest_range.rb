# Longest Range
# https://github.com/WomenWhoCodeNYC/Algorithms/blob/master/challenges/longestRange/longestRange.md
# Write a function that accepts as input an array of integers and then returns the length
# of the longest consecutive range of integers that appear somewhere in that array.
# Write another function that returns the numbers in the range themselves

# sort the array
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
  w = 0
  count = 0
  until i == arr.length
    if arr[i] - 1 == arr[i-1]
      w += 1
    end
    
  end
  count + 1
end

arr = [16, 6, 12, 5, 4, 10, 2, 11, 13, 3, 15]
p longest_range(arr)
