def tax(won):
    money = 0
    if won <= 1200:
        money = won * 0.06
    elif won <= 4600:
        money = 1200 * 0.06 + (won - 1200) * 0.15
    else:
        money = 1200 * 0.06 + (4600 - 1200) * 0.15 + (won - 4600) * 0.24
    return money

print(tax(1200))
print(tax(4600))
print(tax(5000))
