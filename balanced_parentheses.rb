def balanced_parentheses?(str)
  arr = []
  i = 0
  while i < str.length
    if str[i] == "("
      arr << "("
    elsif str[i] == ")" && arr.last == "("
      arr.pop
    else
      return false
    end
    i += 1
  end
  arr.empty?
end


# test inputs
p balanced_parentheses?("(()()()())") == true
p balanced_parentheses?("(((())))") == true
p balanced_parentheses?("(()((())()))") == true
p balanced_parentheses?("((((((())") == false
p balanced_parentheses?("()))") == false
p balanced_parentheses?("(()()(()") == false
