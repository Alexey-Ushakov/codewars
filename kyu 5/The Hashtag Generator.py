def generate_hashtag(s):
    if s is "":
        return False
    else:
        list_s = []
        for i in s.split():
            list_s.append(i.capitalize())
        result = "".join(list_s)
        if len(result) > 140:
            return False
        else:
            return "#" + result


def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output

def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False

def generate_hashtag(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False

def generate_hashtag(s):
    if not s or len(s)>140:
        return False
    return "#"+''.join(x.capitalize() for x in s.split(' '))

generate_hashtag=lambda d:(lambda b:d>''<b==b[:139]and'#'+b)(d.title().replace(' ',''))

def generate_hashtag(s):
    if len(s) > 140 or not s: return False
    return '#' + ''.join(w.capitalize() for w in s.split())

def generate_hashtag(s):
    return '#' + ''.join([word.title() for word in s.split(' ')]) if s and len(s) <= 140 else False