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

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())


def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)

import re

def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)

def pig_it(text):
    return ' '.join([x[1:]+x[0]+'ay' if x.isalpha() else x for x in text.split()])

import re
def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)

