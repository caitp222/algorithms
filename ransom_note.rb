# from cracking the coding challenge

#!/bin/ruby

magazine = "give me one grand today night"
magazine = magazine.split(" ")
ransom = "give one grand today"
ransom = ransom.split(" ")

def magazine_ransom_note(magazine, ransom)
  m = magazine.length
  n = ransom.length
  if n > m
    return "No"
  else
    usable_words = {}
    m.times do |i|
      if usable_words[magazine[i]]
        usable_words[magazine[i]] += 1
      else
        usable_words[magazine[i]] = 1
      end
    end
    i = 0
    while i < n
      if usable_words[ransom[i]] && usable_words[ransom[i]] > 0
          usable_words[ransom[i]] -= 1
      else
        return "No"
      end
      i += 1
    end
  end
  return "Yes"
end

puts magazine_ransom_note(magazine, ransom)
