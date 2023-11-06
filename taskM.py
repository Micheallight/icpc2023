import math
args = input()
arr = args.split()
A = float(arr[0])
B = float(arr[1])
C = float(arr[2])
x = math.sqrt(B / C)
f = (A * x) / (B + C * x * x)
print(x, f)