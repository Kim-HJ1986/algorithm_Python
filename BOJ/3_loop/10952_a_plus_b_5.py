import sys

valid = True
while valid:
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        valid = False
        break
    print(A + B)
