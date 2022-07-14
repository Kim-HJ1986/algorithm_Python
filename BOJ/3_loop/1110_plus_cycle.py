import sys

a = int(sys.stdin.readline())


def fuction(a, i, NewVal, ChangeVal):
    while True:
        if a != NewVal:
            b = str((int(ChangeVal[0]) + int(ChangeVal[-1])))[-1]
            c = int(ChangeVal[-1] + str(b)[-1])
            NewVal = c
            ChangeVal = str(c)
            if int(ChangeVal) < 10:
                ChangeVal = '0' + ChangeVal
            i += 1
        else:
            print(i)
            break


if a >= 10:
    i = 0
    # NewVal은 새로 만들어진 값을 저장하여 원래 값과 비교, ChangeVal은 새로 만들어진 값을 저장하여 새로운 값을 생성하는 데 쓰임
    NewVal = -1
    ChangeVal = str(a)
    fuction(a, i, NewVal, ChangeVal)

elif a < 10:
    i = 0
    NewVal = -1
    ChangeVal = '0' + str(a)

    fuction(a, i, NewVal, ChangeVal)
