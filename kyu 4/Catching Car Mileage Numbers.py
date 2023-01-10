from typing import List
import re


def digit_followed_by_zeros(number: int) -> int:
    regnumber = re.compile(r'\b\d[0]+\b')
    if regnumber.match(str(number)):
        return 2
    elif regnumber.match(str(number + 1)) or regnumber.match(str(number + 2)):
        return 1
    else:
        return 0


def every_digit_is_the_same_number(number: int) -> int:
    if str(number).count(str(number % 10)) == len(str(number)):
        return 2
    elif str(number + 1).count(str((number % 10) + 1)) == len(str(number + 2)) or str(number + 2).count(
            str((number % 10) + 2)) == len(str(number + 2)):
        return 1
    else:
        return 0

def the_digits_are_sequential_incrementing(number: int) -> int:
    temp_list = number




def is_interesting(number: int, awesome_phrases: List[int]) -> int:
    mark_list = [digit_followed_by_zeros(number),
                 every_digit_is_the_same_number(number),
                 the_digits_are_sequential_incrementing]
    return 1

if __name__ == '__main__':
    is_interesting(number, awesome_phrases)




