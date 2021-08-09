#
# def multi_table(number):
#     a = ""
#     for x in range(1,11):
#         if x == 10:
#             a = a + ('{} * {} = {}'.format(x, number, (number * x)))
#         else:
#             a = a + ('{} * {} = {}\n'.format(x, number, (number * x)))
#     return a
#
#
# def multi_table(number):
#     return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


multi_table = lambda number: '\n'.join('{} * {} = {}'.format(x, number, x * number) for x in range(1, 11))
print(multi_table(7))


