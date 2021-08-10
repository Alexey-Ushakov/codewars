import re
def to_camel_case(text):
    if text == "":
        return text
    else:
        if text[:1].isupper():
            result = re.findall(r'[^_-]+', text)
            string = ''.join(list(map(str.capitalize, result)))
        else:
            result = re.findall(r'[^_-]+', text)
            string = result[0]+''.join(list(map(str.capitalize, result[1:])))
    return string


