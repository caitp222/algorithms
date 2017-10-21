# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# For example, given:
# [1, 7, 3, 4]
# the function should return:
# [84, 12, 28, 21]

def product_of_integers(array)
  i = 0
  x = 0
  new_array = []
  while i < array.length
    memo = 1
    x = 0
    while x < array.length
      memo = memo * array[x] if x != i
      x += 1
    end
    new_array.push(memo)
    i += 1
  end
  new_array
end

p product_of_integers([1, 7, 3, 4]) == [84, 12, 28, 21]
