def dig_pow(n, p):
    result = 0
    for i in str(n):
        result += int(i) ** p
        p += 1
    if result != n * int(result / n):
        return -1
    else:
        return result // n




print(dig_pow(46288, 3))
