import json


def turn(temperatures):
    maximum = []
    minimum = []
    for i in range(len(temperatures)):
        a = temperatures[i][0]
        b = temperatures[i][1]
        if a >= b :
            maximum.append(a)
            minimum.append(b)
        else:
            maximum.append(b)
            minimum.append(a)
    result = { 'maximum': maximum , 'minimum' : minimum}
    return result




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
