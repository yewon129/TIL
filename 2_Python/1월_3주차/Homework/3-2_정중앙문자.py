def get_middle_char(word):
    for char in word:
        if len(word) % 2 == 1:
            return word[len(word) // 2]
        else:
            return word[(len(word)//2)-1 : (len(word)//2) + 1]

print(get_middle_char('ssafy'))
print(get_middle_char('coding'))
