def get_secret_number(name):
    secret_number = 0
    for element in name:
        secret_number += ord(element)
    return secret_number

print(get_secret_number('tom'))