# http://www.techiedelight.com/find-possible-combinations-words-formed-from-mobile-keypad/

def mobile_keypad(input, ans=[]):
    keypad = {
        2: ["A","B","C"],
        4: ["G","H","I"],
        3: ["D","E","F"],
        5: ["J","K","L"],
        6: ["M","N","L"],
        7: ["P","Q","R","S"],
        8: ["T","U","V"],
        9: ["W","X","Y","Z"]
    }
    if len(input) == 0:
        return ans
    else:
        for x in range(0, len(input) - 1):
            ans.append(keypad[input[x]] + mobile_keypad(input[1:], ans))
        return ans


print mobile_keypad([2,3,4])
