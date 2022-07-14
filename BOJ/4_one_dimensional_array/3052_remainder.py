import sys

remainder_arr = [0 for i in range(10)]

for i in range(10):
    num = int(sys.stdin.readline())
    remainder_arr[i] = num % 42

remainder_arr = set(remainder_arr)
print(len(remainder_arr))
