def get_dict_avg(scores):
    total = 0
    cnt = 0
    for key in scores:
        total += scores.get(key)
        cnt += 1
    return total/cnt

print(get_dict_avg({'python':80, 'a':90,'d':89,'b':83}))