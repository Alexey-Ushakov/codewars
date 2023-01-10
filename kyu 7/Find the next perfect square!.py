def find_next_square(sq):
    if sq**(1/2) % 1 == 0:
        return (sq**(1/2) + 1) ** 2
    # Return the next square if sq is a square, -1 otherwise
    else:
        return -1

def find_next_square(sq):
    x = sq**0.5
    return -1 if x % 1 else (x+1)**2