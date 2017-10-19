# Given a non-empty string like "Code" return a string like "CCoCodCode".
# stringSplosion("Code") → "CCoCodCode"
# stringSplosion("abc") → "aababc"
# stringSplosion("ab") → "aab"

def string_splosion(str)
  new_str = ""
  i = 0
  until i == str.length
    new_str << str[0..i]
    i += 1
  end
  new_str
end

p string_splosion("Code")
p string_splosion("abc")
p string_splosion("ab")
