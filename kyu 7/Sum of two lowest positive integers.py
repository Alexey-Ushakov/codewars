def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])



numbers = [5, 8, 12, 18, 22]

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))