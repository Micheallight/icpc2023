args = input()
arr = args.split()
p = int(arr[0])
q = int(arr[1])
a = int(arr[2])
taler = a / (p * q + q + 1)
gold = taler * p * q
silver = taler * q
cuprum = taler
print(int(gold), int(silver), int(cuprum))