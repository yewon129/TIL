def count_blood(blood):
    A = blood.count('A')
    B = blood.count('B')
    O = blood.count('O')
    AB = blood.count('AB')
    return {'A' : A, 'B' :B,'O' : O,'AB' : AB}

print(count_blood(['A','B','AB','O','A']))