# https://leetcode.com/problems/two-sum/description/

def two_sum(arr, int)
  i = 0
  w = 0
  while i < arr.length
    while w < arr.length
      if w != i && (arr[i] + arr[w] == int)
        return [i, w]
      end
      w += 1
    end
    i += 1
  end
end

# refactored for speed
def two_sum_second(arr, int)
  i = 0
  while i < arr.length
    x = int - arr[i]
    if arr.include?(x)
      return [i, arr.find_index(x)]
    else
      return nil
    end
    i += 1
  end
end

nums = [2, 7, 11, 15]
target = 9

p two_sum(nums, target)
p two_sum_second(nums, target)
