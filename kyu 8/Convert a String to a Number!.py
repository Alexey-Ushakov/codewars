def digitize(n):
    return map(int, str(n)[::-1])

def digitize(n):
    return [int(x) for x in str(n)[::-1]]
