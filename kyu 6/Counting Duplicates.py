def duplicate_count(text):
    unique_letters = set(text.lower())
    result = 0
    for letter in unique_letters:
        if text.lower().count(letter) >= 2:
            result += 1
    return result

print(duplicate_count("tText4X5T"))

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

from collections import Counter

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)

from collections import Counter

def duplicate_count(text):
    counter = Counter(text.lower())
    return len([counter.keys() for i in counter.values() if i>1])

from collections import Counter

def duplicate_count(text):
    return sum(v > 1 for v in Counter(text.lower()).itervalues())

from re import findall

def duplicate_count(text):
    return (len(findall("(\w)\\1+", "".join(sorted(text.upper())))))