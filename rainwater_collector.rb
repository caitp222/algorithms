# https://github.com/WomenWhoCodeNYC/Algorithms/blob/master/challenges/rainWaterCollector/rainWaterCollector.md

def rain_calculator(array)
  total = 0
  i = 1
  loop do
    first = array.find_index{|num| num == i}
    last = array.rindex{|num| num == i}
    if !first || !last || array[first..last].length < 2
      return total
      break
    else
      total += array[first..last].select{|num| num < i}.length
      i += 1
    end
  end
end
