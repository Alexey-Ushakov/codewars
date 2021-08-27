
def duplicate_count(text):
    unique_letters = set(text.lower())
    result = 0
    for letter in unique_letters:
        if text.lower().count(letter) >= 2:
            result += 1
    return result


print(duplicate_count("tText4X5T"))

