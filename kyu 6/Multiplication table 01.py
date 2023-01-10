def multiplication_table(size):
    a = []
    for i in range(1, size+1):
        a.append([j*i for j in range(1, size+1)])
    print(a)

multiplication_table(3)

def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]