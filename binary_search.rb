def binary_search(item, arr)
  p arr
  max = arr.length-1
  p "max: #{max}"
  min = 0
  p "mid"
  p mid = (max + min)/2
  p "max == mid"
  p max == mid
  return nil if min == max

  if item == arr[mid]
    return mid
  end

  if item > arr[mid]
    p "item greater than mid"
    min = mid
    p min
  else
    p "item less than mid"
    max = mid
    p max
  end

  binary_search(item, arr[min..max])

end

sorted_array = [497]
desired_length = 18
until
  sorted_array.length == desired_length
  sorted_array.push(rand(1..1000))
  sorted_array.sort!
end

p sorted_array
p sorted_array.find_index(497)
p binary_search(497, sorted_array)
