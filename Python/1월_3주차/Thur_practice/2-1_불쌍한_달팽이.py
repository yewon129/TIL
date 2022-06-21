## 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다. (낮 시간 동안 올라간 거리보다는 적게 미끄러진다.)
##달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 snail()을 작성하시오.
#1. 기둥의 높이(미터)
#2. 낮 시간 동안 달팽이가 올라가는 거리(미터)
#3. 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

def snail(height,day,night):
    length = 0
    count = 0
    while length < height :
        length += day
        count += 1
        if length < height:
            length -= night

    return count

print(snail(100,5,2))
