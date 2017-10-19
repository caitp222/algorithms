# A “word square” is an ordered sequence of K different words of length K that,
# when written one word per line, reads the same horizontally and vertically.
# For example:
word_sq = ["BALL","AREA","LEAD","LADY"]
# First, design a way to return true if a given sequence of words is a word square.

def is_word_sq?(arr)
  arr1 = []
  arr.length.times do
    arr1 << ""
  end
  i = 0
  until i == arr.length
    arr.each do |word|
      arr1[i] << word[i] unless !word[i]
    end
    i += 1
  end
  arr1 == arr
  # arr1 = arr.map { |word| word.chars }
  # arr2 = arr1.transpose
  # arr2 == arr.map { |word| word.chars }
end

p is_word_sq?(word_sq)

# Second, given an arbitrary list of words, return all the possible word squares it contains.
# Reordering is allowed.
# For example, the input list:
arr = ["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]
# should output
# [(BALL, AREA, LEAD, LADY), (LADY, AREA, DEAR, YARD)]
