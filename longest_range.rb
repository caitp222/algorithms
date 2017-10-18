# Longest Range
# https://github.com/WomenWhoCodeNYC/Algorithms/blob/master/challenges/longestRange/longestRange.md

# first define a sort method
require_relative 'bubble_sort.rb'

# longest range method
def longest_range_length(arr)
  bubble_sort(arr)
  new_arr = []
  max_length = 1
  i = 0
  until i == arr.length
    if arr[i] - 1 == arr[i-1]
      if new_arr.length == 0
        new_arr << arr[i-1]
      end
      new_arr << arr[i]
    elsif arr[i] - 1 != arr[i-1]
      if new_arr.length > max_length
        max_length = new_arr.length
      end
      new_arr = []
    end
    i += 1
  end
  max_length
end

# refactor to return an array
def longest_range_elements(arr)
  bubble_sort(arr)
  new_arr = []
  max_length = 1
  i = 0
  until i == arr.length
    if arr[i] - 1 == arr[i-1]
      if new_arr.length == 0
        new_arr << arr[i-1]
      end
      new_arr << arr[i]
    elsif arr[i] - 1 != arr[i-1]
      if new_arr.length > max_length
        max_length = new_arr.length
        longest_arr = new_arr
      end
      new_arr = []
    end
    i += 1
  end
  longest_arr
end

arr1 = [16, 6, 12, 5, 4, 10, 2, 11, 13, 3, 15]
p longest_range_length(arr1)
p longest_range_elements(arr1)
arr2 = [2, 29, 26, 22, 23, 57, 3, 4, 27, 21, 25, 5, 28, 1, 60, 24, 56, 67, 58, 61]
p longest_range_length(arr2)
p longest_range_elements(arr2)
