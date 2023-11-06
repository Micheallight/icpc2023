# input(arg)
# print("hello")

# import argparse
# parser = argparse.ArgumentParser(description='A tutorial of argparse!')
# parser.add_argument("--a")
# args = parser.parse_args()
# a = args.a
# print(a)

# a = int(input())
# b = int(input())
# print(a, b)

# ### 1

# import argparse

# parser = argparse.ArgumentParser(
# 	prog = 'Even numbers',
# 	description='Printing even numbers less than argument'
# 	)

# parser.add_argument(
# 	'integers', 
# 	type=int, 
# 	nargs='+'
# 	)
# args = parser.parse_args()

# # print(", ".join(map(str, range(2, max(args.integers), 2))))
# print(args.integers)

args = input()
arr = args.split()
res = int(arr[0]) * int(arr[1]) / 100
res = int(round(res, 0))
print(res)