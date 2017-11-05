def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[-1]
        less = []
        more = []
        for x in lst:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                more.append(x)
        return quicksort(less) + [pivot] + quicksort(more)

list_to_sort = [9,-3,5,2,6,8,-6,1,3]
print quicksort(list_to_sort)
