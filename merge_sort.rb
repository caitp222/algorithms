def merge_sort(arr, low=0, high=arr.length-1)
  if low == high
    return arr
  else
    mid = (low + high)/2
    merge(merge_sort(arr[low..mid]), merge_sort(arr[mid+1..high]))
  end
end

def merge(arr1, arr2)
  new_arr = []
  until arr1.empty? || arr2.empty?
    if arr1.first < arr2.first
      new_arr << arr1.delete_at(0)
    elsif arr1.first > arr2.first
      new_arr << arr2.delete_at(0)
    end
  end
  new_arr.concat(arr1).concat(arr2)
end

arr = [38,27,43,3,9,82,10]
p merge_sort(arr)
