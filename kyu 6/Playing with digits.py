# def dig_pow(n, p):
#     result = 0
#     for i in str(n):
#         result += int(i) ** p
#         p += 1
#     if result != n * int(result / n):
#         return -1
#     else:
#         return result // n

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1