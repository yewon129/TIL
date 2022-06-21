def get_secret_word(numbers):
    secret_number = ''
    for number in numbers:
        secret_number += chr(number)
    return secret_number

print(get_secret_word([83,115,65,102,89]))