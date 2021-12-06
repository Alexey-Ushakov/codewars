# def are_coprime(n,m):
#     lstn = []
#     lstm = []
#     for i in range(2, n + 1):
#         if n % i == 0:
#             lstn.append(i)
#     for i in range(2, m + 1):
#         if m % i == 0:
#             lstm.append(i)
#     print(lstn, lstm)
#     for i in lstn:
#         if i in lstm:
#             return False
#     return True

def are_coprime(n, m):
    # All hail Euclid and his wonderful algorithm
    while m > 0:
        n, m = m, n % m
    return n == 1

# def are_coprime(x,y):
#     arrX = [i for i in range(1, x + 1) if x % i == 0]
#     arrY = [i for i in range(1, y + 1) if y % i == 0]
#     return len(list(set(arrX) & set(arrY))) == 1
#
# def are_coprime(n,m):
#     while n%m != 0:
#         n, m = m, n%m
#     if m == 1: return True
#     else: return False


print(are_coprime(15, 27))

