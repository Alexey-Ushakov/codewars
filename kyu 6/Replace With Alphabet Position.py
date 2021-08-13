import string
def alphabet_position(text):
    list_of_number = []
    for i in text:
        for num, char in enumerate(string.ascii_lowercase, 1):
            if i.lower() == char:
                list_of_number.append(str(num))
    result = ' '.join(list_of_number)
    return result



