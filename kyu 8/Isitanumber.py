def isDigit(string):
    try:
        a = float(string)
    except Exception:
        return False
    else:
        return True