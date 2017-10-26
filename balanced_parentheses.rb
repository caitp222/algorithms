def balanced_parentheses?(str, min=0, max=str.length-1)
  if !min || !max
    return false
  elsif 
  end
end


# test inputs
p balanced_parentheses?("(()()()())") == true
p balanced_parentheses?("(((())))") == true
p balanced_parentheses?("(()((())()))") == true
p balanced_parentheses?("((((((())") == false
p balanced_parentheses?("()))") == false
p balanced_parentheses?("(()()(()") == false
