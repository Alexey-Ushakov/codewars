def multiplication_table(row,col):
    all = []
    data = 0
    for i in range(row):
        cell = []
        all.append(cell)
        data += 1
        for j in range(1, col+1):
            all[i].append(data * j)
    print(all)

def multiplication_table(row,col):
    return [[(i+1)*(j+1) for j in range(col)] for i in range(row)]