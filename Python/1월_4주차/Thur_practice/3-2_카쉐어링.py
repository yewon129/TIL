import math

def fee(minute, distance):
    money = 0
    money += (minute//10) * 1200
    money += math.ceil(minute/30) * 525
    if distance <= 100:
        money += distance * 170
    else :
        money += 100 * 170 + (distance-100) * 85
    return money

print(fee(600, 50))
print(fee(600, 110))