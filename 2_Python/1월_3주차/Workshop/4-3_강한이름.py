def get_strong_word(a,b):
    total_a = 0
    for i in a:
        total_a += ord(i)
    total_b = 0
    for j in b:
        total_b += ord(j)
    if total_a > total_b:
        return a
    else:
        return b

print(get_strong_word('tom','john'))