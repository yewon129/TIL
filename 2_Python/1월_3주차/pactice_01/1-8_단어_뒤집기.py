## 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오

word = input()

number = len(word)
new_word = []
for i in range(number):
    new_word.append(word[-(i+1)])

for alphabet in new_word:
    print(alphabet, end='')