def max_span(arr)
  # start with arr[0], check if the element repeats at arr.last, then at arr-1
  i = 0
  w = arr.length-1
  max_span = 1
  while i < arr.length
    until w == i
      if arr[i] == arr[w]
        if (w - i + 1) > max_span
          max_span = (w - i + 1)
        end
      end
      w = w - 1
    end
    w = arr.length - 1
    i += 1
  end
  max_span
end

p max_span([1, 4, 2, 1, 4, 4, 4])
p max_span([1, 2, 1, 1, 3]) == 4
p max_span([1, 4, 2, 1, 4, 1, 4]) == 6
p max_span([1, 4, 2, 1, 4, 4, 4]) == 6
