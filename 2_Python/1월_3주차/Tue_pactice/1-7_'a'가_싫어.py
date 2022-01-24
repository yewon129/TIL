## 입력으로 짧은 영단어 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과를 출력하시오.

word = input()

new_word = ''
for alphabet in word:
    if alphabet != 'a':
        new_word += alphabet

print(new_word)