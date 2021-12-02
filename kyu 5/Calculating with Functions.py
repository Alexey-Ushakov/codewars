# def zero(f=None): return 0 if f is None else int(f(0))
# def one(f=None): return 1 if f is None else int(f(1))
# def two(f=None): return 2 if f is None else int(f(2))
# def three(f=None): return 3 if f is None else int(f(3))
# def four(f=None): return 4 if f is None else int(f(4))
# def five(f=None): return 5 if f is None else int(f(5))
# def six(f=None): return 6 if f is None else int(f(6))
# def seven(f=None): return 7 if f is None else int(f(7))
# def eight(f=None): return 8 if f is None else int(f(8))
# def nine(f=None): return 9 if f is None else int(f(9))
#
# def plus(y): return lambda x: x + y
# def minus(y): return lambda x: x - y
# def times(y): return lambda x: x * y
# def divided_by(y): return lambda x: x / y


id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y // x

# print(seven(plus(five())))
# print(plus('five')('seven'))

# number():
#  - expects a number "A"
#  - returns a function "F" that expects a single argument function (or if not provided it uses "id_" by default)
# Когда оба аргумента предоставлены, функция number() вычисляется и применяет функцию F к числу A
#
# # Example 1: returns only 3 (applies "id_" by default)
print(number(3)())
# Печать:
#
# 3
# И когда функция предоставляется:
#
def inc(x):
    return x + 1
#
# # Example 2: applies a single argument function to the number 3
print(number(3)(inc))
# Который возвращает:
#
# 4
# Итак, теперь вторая функция, которая вас интересует:
#
# plus():
#  - expects a number
#  - returns a function that accept another number
# Когда оба аргумента предоставлены, функция вычисляется и возвращает их сумму.
#
# # Example:
print(plus(3)(4))
# Печать:
#
# 7
# Используя пример, который вы использовали в комментариях:
#
# one(plus(one()))
# Начиная с самого сокровенного выражения, которое мы получаем:
#
# one() == 1 because one() == number(1)(f=id_) == id_(1)
#
# Второй вызов plus(1) вернет lambda y: y+1
#
# Применяется к результату с первого шага, plus(one()) == plus(1) == lambda y: y+1
#
# Таким образом, это означает, что plus(one()) (другими словами: "returns") сам по себе является функцией и эквивалентен:
#
# def plus_one(y):
#    return y + 1
# Последний шаг:
# one(plus(one())) == one(plus_one) == number(1)(f=plus_one) == plus_one(1) == 1 + 1 == 2
#
# Если синтаксис lambda вас беспокоит, вы можете переписать их для большей ясности (?) В полные функции соответственно:
#
# def id_(x):
#     return x
#
# def number(x):
#     def inner(f=id_):
#         return f(x)
#
#     return inner
#
# def one(f=id_):
#     return f(1)
#
# def plus(x):
#     def add_to_x(y):
#         return y + x
#
#     return add_to_x
#
# add_one = plus(one())
#
# assert one() == number(1)(f=id_) == id_(1) == 1
#
# assert add_one(2) == plus(1)(2) == 3
#
# assert plus(one())(4) == plus(1)(4) == 5
#
# assert one(plus(one())) == one(add_one) == 2