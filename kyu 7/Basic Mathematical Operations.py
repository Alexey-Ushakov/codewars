def basic_op(operator, value1, value2):
    operator_dict = {'-': value1 - value2,
                     "+": value1 + value2,
                     "*": value1 * value2,
                     "/": value1 / value2,
    }
    return operator_dict[operator]

def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)

def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')