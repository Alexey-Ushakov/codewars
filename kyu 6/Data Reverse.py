data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
ls = []
for _ in range(4):
    byte = []
    for _ in range(8):
        bit = data1.pop(0)
        byte.append(bit)
    ls.append(byte)
ls.reverse()
for j in ls:
    print("".join(map(str, j)), end=" ")
# "".join(str(data1[i]) for i in range(len(data1)-1,-1, -1))

