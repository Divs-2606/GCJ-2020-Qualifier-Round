tstc = int(input())
def gK1(values):
    return values[2]
def gK00(values):
    return values[0]
A1 = []
B1 = []
for i in range(tstc):
    n = int(input())
    A1.clear()
    for j in range(n):
        B1 = []
        B1 = [int(y) for y in input().split(" ")]
        B1.append(j)
        A1.append(B1)
    A1.sort(key=gK00)
    j_count = -1
    c_count = -1
    f = True
    for y in A1:
        t_s = y[0]
        t_e = y[1]
        if c_count == -1:
            c_count = t_e
            y.append('C')
        elif t_s >= c_count:
            c_count = t_e
            y.append('C')
        elif t_s< c_count and t_s >= j_count:
            j_count = t_e
            y.append('J')
        elif t_s < c_count and t_s < j_count:
            f = False
            break
    if f == False:
        out = "IMPOSSIBLE"
    else:
        out = ""
        A1.sort(key = gK1)
        out = out.join([y[3] for y in A1])
    print("Case #{}: {}".format(i+1,out))