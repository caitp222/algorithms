# http://codingbat.com/prob/p121193

def sum_numbers(str)
  arr = str.scan(/\d*/)
  memo = 0
  arr.map do |str|
    if str.length > 0
      memo += str.to_i
    end
  end
  memo
end

p sum_numbers("abc123xyz")
p sum_numbers("aa11b33")
p sum_numbers("7 11")
p sum_numbers("abc123xyz") == 123
p sum_numbers("aa11b33") == 44
p sum_numbers("7 11") == 18
