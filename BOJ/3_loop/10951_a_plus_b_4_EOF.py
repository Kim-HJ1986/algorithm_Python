import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    # try-catch 와 같은 구조임. error, exception 발생 시 except로 잡힘
    except:
        break
