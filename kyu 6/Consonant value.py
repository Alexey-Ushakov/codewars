import string
import re

def solve(s):
    """replace all Consonant value with a " "(space) """
    empty = []
    result = re.sub(r'[AEIOU]', ' ', s, flags=re.IGNORECASE)

    solution = result.split(" ")
    for i in range(len(solution)):
        alphabet = string.ascii_lowercase  # латинский алфавит
        word = solution[i]
        ind_list = [sum(alphabet.index(x) + 1 for x in word.lower())]
        empty.append(' '.join(map(str, ind_list)))

    print(max(map(int, empty)))