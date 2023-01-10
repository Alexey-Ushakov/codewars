def chained(functions):
    def g(x): #curry the functions
        result = x
        for f in functions:
            result = f(result)
        return result
    return g


# def chained(functions):
#     def g(x): #curry the functions
#         for f in functions:
#             x = f(x)
#         return x
#     return g


def f1(x): return x*2
def f2(x): return x+2
def f3(x): return x**2

def f4(x): return x.split()
def f5(xs): return [x[::-1].title() for x in xs]
def f6(xs): return "_".join(xs)

print(chained([f1, f2, f3])(0))

