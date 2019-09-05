def triangles():
    r = [1]
    while True:
        l = r
        print('BBBBBBB',l)
        yield r[:]
        for i in range(0, len(l) - 1):
            r[i + 1] = l[i] + l[i + 1]
        r.append(1)
        print('AAAAAAAA',r)
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)