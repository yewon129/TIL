def duplicated_letter(word):
    result = []
    for element in word:
        if word.count(element) >= 2 :
            if element not in result:
                result.append(element)
    return result

print(duplicated_letter('apple'))
print(duplicated_letter('banana'))
