import math

def h(a, b, c):
    res = (abs((c[1] - b[1]) * a[0] + (c[0] - b[0]) * a[1] + b[1] * (c[0] - b[0]) - b[0] * (c[1] - b[1]))) / (math.sqrt(math.pow(c[1] - b[1], 2) + math.pow(c[0] - b[0], 2))) * (1 - 1 / math.sqrt(2))
    return res

num = int(input())
i = 0
results = []
while i < num:
    in_a = input()
    in_b = input()
    in_c = input()
    a = [int(in_a.split()[0]), int(in_a.split()[1])]
    b = [int(in_b.split()[0]), int(in_b.split()[1])]
    c = [int(in_c.split()[0]), int(in_c.split()[1])]
    ha = h(a, b, c)
    hb = h(b, a, c)
    hc = h(c, a, b)
    results.append([ha, hb, hc])
    i += 1
i = 0
while i < num:
    print(results[i])
    i += 1

