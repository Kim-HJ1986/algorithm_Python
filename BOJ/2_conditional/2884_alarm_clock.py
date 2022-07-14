hh, mm = map(int, input().split())

if mm >= 45:
    mm -= 45
    print(hh, mm)
else:
    if hh <= 0:
        hh += 23
    else:
        hh -= 1
    mm += 15
    print(hh, mm)

