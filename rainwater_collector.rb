# https://github.com/WomenWhoCodeNYC/Algorithms/blob/master/challenges/rainWaterCollector/rainWaterCollector.md

def rain_calculator(arr)
  water = 0
  height = 1
  max = max_height(arr)
  until height == max
    first = arr.find_index{|num| num >= height}
    last = arr.rindex{|num| num >= height}
    water += arr[first..last].select{|num| num < height}.length
    height += 1
  end
  water
end

def max_height(arr)
  i = 0
  max = 0
  while i < arr.length
    if arr[i] > max
      max = arr[i]
    end
    i += 1
  end
  max
end

arr1 = [7,0,4,2,5,0,6,4,0,5]
# should return 25
arr2 = [0,1,0,2,1,0,1,3,2,1,2,1]
# should return 6
p rain_calculator(arr1)
p rain_calculator(arr2)
