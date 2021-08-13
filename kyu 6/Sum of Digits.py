def digital_root(n):
    while len(str(n)) != 1:
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
    return n
