def dict_list_sum(my_list):
    sum_age = 0
    for dict in my_list:
        sum_age +=dict.get('age')
    return sum_age

print(dict_list_sum([{'name':'kim','age':12}, {'name':'lee','age':4}]))