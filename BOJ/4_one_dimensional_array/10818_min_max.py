import sys

N = int(input())
num_arr = list(map(int, sys.stdin.readline().split()))

print(min(num_arr), max(num_arr))
