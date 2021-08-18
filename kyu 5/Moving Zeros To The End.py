def move_zeros(array):
    list_of_zero = []
    list_of_number = []
    for i in array:
        if i == 0:
            list_of_zero.append(i)
            print(list_of_zero)
        else:
            list_of_number.append(i)
    return list_of_number + list_of_zero

