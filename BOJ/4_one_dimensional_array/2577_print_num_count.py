
A = int(input())
B = int(input())
C = int(input())

ABC_arr = list(str(A * B * C))

# 10개의 0으로 이루어진 배열 생성
num_arr = [0 for i in range(10)]

for num in ABC_arr:
    num_arr[int(num)] += 1

for num in num_arr:
    print(int(num))

