def dict_invert(my_dict):
    result = {}
    for key,value in my_dict.items():
        result[value] = result.get(value,[]) + [key]
    return result

print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))