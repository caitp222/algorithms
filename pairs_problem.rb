def pairs(arr)
  hash = {}
  arr.each do |word|
    hash[word[0]] = word[word.length-1]
  end
  hash
end

p pairs(["code", "bug"]) == {"b" => "g", "c" => "e"}
p pairs(["man", "moon", "main"]) == {"m" => "n"}
p pairs(["man", "moon", "good", "night"]) == {"g" => "d", "m" => "n", "n" => "t"}
