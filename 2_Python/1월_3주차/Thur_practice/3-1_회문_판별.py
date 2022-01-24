## 회문 또는 팰린드롬은 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열 등을 말한다.
## 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어가 회문이면 True 회문이 아니면 False를 반환하는 함수를 작성하시오.
## 이때, 반복문(while)과 재귀 함수를 사용해서 각각 작성하시오.

def is_pal_while(word):
    length = len(word)
    for i in range(length):
        while word[i] != word[-(i+1)]:
            return False
        else:
            return True



print(is_pal_while('tomato'))
print(is_pal_while('racecar'))
print(is_pal_while('azza'))