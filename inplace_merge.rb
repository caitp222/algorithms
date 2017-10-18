# to be done in place and not using any other data structure

def inplace_merge(arr1, arr2)
  i = 0
  w = 0
  while i < arr1.length
    while w < arr2.length
      if arr1[i] > arr2[w]
        temp = arr1[i]
        arr1[i] = arr2[w]
        arr2[w] = temp
        sort_array(arr2)
      end
      w += 1
    end
    i += 1
    w = 0
  end
  "#{arr1}, #{arr2}"
end

def sort_array(arr)
  # assuming only one element is out of position
  i = 0
  while i < arr.length - 1
    if arr[i] > arr[i+1]
      arr[i], arr[i+1] = arr[i+1], arr[i]
    end
    i += 1
  end
  arr
end

arr1 = [1,4,7,8,10]
arr2 = [2,3,9]
p inplace_merge(arr1, arr2)
