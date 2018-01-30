def solution(message, length):
    lst = message.split(" ")
    texts = []
    new_text = []
    while len(lst) > 0:
        if (len("".join(new_text)) + len(new_text) + len(lst[0])) <= length:
            new_text.append(lst[0])
            del(lst[0])
            if len(lst) == 0:
                texts.append(new_text)
        else:
            texts.append(new_text)
            new_text = []
    return len(texts)

print(solution('SMS messages are very short', 12))
print(solution('Where are we going today? Do you want to go home? What the fuck is your problem?', 12))
