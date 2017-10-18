def binary_search(item, arr, min=0, max=arr.length)
  mid = (max + min)/2
  if item > arr[mid]
    min = mid + 1
    binary_search(item, arr, min, max)
  elsif item < arr[mid]
    max = mid - 1
    binary_search(item, arr, min, max)
  elsif item == arr[mid]
    return mid
  end
end

# need to refactor to detect if item isn't in array

sorted_array = [789]
desired_length = 18
until
  sorted_array.length == desired_length
  sorted_array.push(rand(1..1000))
  sorted_array.sort!
end

p sorted_array
p "number is at index #{sorted_array.find_index(789)}"
p binary_search(789, sorted_array)
