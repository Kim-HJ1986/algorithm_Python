a, b = map(int, input().split())


def comparator(a, b):
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")


comparator(a, b)
