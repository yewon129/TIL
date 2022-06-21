from xml.etree import ElementInclude


def all_list_sum(my_list):
    total = 0
    for element in my_list:
        for i in element:
            total += i
    return total

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))
