def digital_root(n):
    while len(str(n)) != 1:
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
    return n

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):
    return n%9 or n and 9

def digital_root(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n

def digital_root(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root