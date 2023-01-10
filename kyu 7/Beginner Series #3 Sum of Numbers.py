def get_sum(a,b):
    numbers =sorted([a, b])
    if sum(range(numbers[0], numbers[1], 1)) == 0:
        return b
    else:
        return sum(range(numbers[0], numbers[1], 1))

print(get_sum(0,1))


def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
