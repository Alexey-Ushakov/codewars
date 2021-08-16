import copy
def pig_it(text):
    list_of_text = text.split(" ")
    list_of_result = []
    for i in copy.copy(list_of_text):
        if i not in ["!", '?']:
            a = i[1:] + i[0] +'ay'
            list_of_result.append(a)
        else:
            a = i
            list_of_result.append(a)
    return ' '.join(list_of_result)


