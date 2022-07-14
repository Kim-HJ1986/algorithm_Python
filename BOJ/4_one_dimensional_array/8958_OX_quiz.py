import sys

T = int(input())

for i in range(T):
    OX_arr = list(sys.stdin.readline())
    score = 0
    sum = 0
    for OX in OX_arr:
        if OX == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
