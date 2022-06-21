def count_vowels(word):
    vowels = ['a','e','i','o','u']
    cnt = 0
    for vowel in vowels:
        cnt += word.count(vowel)
    return cnt

print(count_vowels('apple'))
