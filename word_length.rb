def word_length(arr)
  hash = {}
  arr.each do |word|
    hash[word] = word.length
  end
  hash
end

p word_length(["a", "bb", "a", "bb"]) == {"bb" => 2, "a" => 1}
p word_length(["this", "and", "that", "and"]) == {"that" => 4, "and" => 3, "this" => 4}
p word_length(["code", "code", "code", "bug"]) == {"code" => 4, "bug" => 3}
