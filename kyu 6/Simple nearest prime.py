#  Мои решения были слишком долгие ( зато нашел ошибку у всех 15 было простым числом по итогу никто не решил верно кроме тех кто использовал сторонние библиотеки
# def solve(n):
#     lst = [2]
#     for i in range(3, n + 100, 2):
#         if (i > 10) and (i % 10 == 5):
#             continue
#         for j in lst:
#             if j * j - 1 > i:
#                 lst.append(i)
#
#                 break
#             if (i % j == 0):
#                 break
#         else:
#             lst.append(i)
#         if i > n:
#             break
#     print(lst)
# solve(10000)



def solve(n):
    print('starting with {0}'.format(n), flush=True)

    def is_prime(p):
        if p % 2 == 0 :
            return False
        for x in range(3, int(p**.5)+1):
            if p % x == 0:
                return False
        return True


    if is_prime(n):
        return n
    step = (n%2) + 1
    while 1:
        if is_prime(n-step):
            return n-step
        elif is_prime(n+step):
            return n+step
        else:
            step += 2
    return None

print(solve(15))


