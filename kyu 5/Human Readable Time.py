def make_readable(seconds):
    return "{:02}:{:02}:{:02}".format(seconds//3600, seconds % 3600 // 60, seconds % 60)

print(make_readable(86399))