def move_zeros(array):
    list_of_zero = []
    list_of_number = []
    for i in array:
        if i == 0:
            list_of_zero.append(i)
        else:
            list_of_number.append(i)
    return list_of_number + list_of_zero

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)


def move_zeros(array):
    newarr = []
    zeroarr = []
    for item in array:
        if item != 0 or type(item) == bool:
            newarr.append(item)
        else:
            zeroarr.append(item)

    newarr.extend(zeroarr)
    return (newarr)

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


def move_zeros(array):
    return [a for a in array if isinstance(a, bool) or a != 0] + [a for a in array if
                                                                  not isinstance(a, bool) and a == 0]

def move_zeros(array):
    return sorted(array, key= lambda x: x == 0 and type(x) != bool)

def move_zeros(array):
    a = list(filter(lambda x: x!=0 or type(x) is bool, array))
    return a + [0]*(len(array)-len(a))

def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a