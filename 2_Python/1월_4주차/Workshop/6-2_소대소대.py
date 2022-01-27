def low_and_up(word):
    new_word = ''
    for i in range(len(word)):
        if i % 2 == 0 :
            new_word += word[i].lower()
        elif i % 2 == 1:
            new_word += word[i].upper()
    return new_word

print(low_and_up('banana'))