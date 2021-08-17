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


