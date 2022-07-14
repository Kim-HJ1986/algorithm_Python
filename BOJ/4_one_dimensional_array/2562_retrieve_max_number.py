import sys

max_num_value = 0
max_num_index = 0
for i in range(1,10):
    num = int(sys.stdin.readline())
    if num > max_num_value:
        max_num_value = num
        max_num_index = i

print(max_num_value)
print(max_num_index)