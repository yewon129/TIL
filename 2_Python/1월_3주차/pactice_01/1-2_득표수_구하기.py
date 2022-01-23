## 주어진 리스트는 반장 선거 투표 결과이다. 이영희의 총 득표수를 출력하시오.

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

count = 0
for student in students :
    if student == '이영희':
        count += 1
    else :
        pass

print(count)