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


def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)

def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])

def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''