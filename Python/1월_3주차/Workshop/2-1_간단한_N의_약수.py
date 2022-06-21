number = int(input())

factor = []
for i in range(1,number+1):
    if number % i == 0:
        factor.append(i)

for i in factor:
    print(i, end=' ')