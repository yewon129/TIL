import json


def max_score(scores):
    max_score = scores[0]
    for i in range(len(scores)):
        if max_score < scores[i]:
            max_score = scores[i]
            i += 1
        else :
            pass
    return max_score


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
