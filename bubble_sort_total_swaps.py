# bubble sort re-done in python and keeping track of total swaps


def bubble_sort(lst):
  sorted = False
  total_swaps = 0
  while sorted is False:
    current_swaps = 0
    i = 0
    while i < len(lst) - 1:
      if lst[i] > lst[i + 1]:
        memo = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = memo
        current_swaps += 1
      i += 1
    if current_swaps is 0:
      sorted = True
    else:
      total_swaps += current_swaps
  print("Sorted in %s swaps" % (str(total_swaps)))
  print("The first element in the array is %s" % (str(lst[0])))
  print("The last element in the array is %s" % (str(lst[-1])))

  
lst = [4,8,7,1,4,9,0,3,5]
print(bubble_sort(lst))
