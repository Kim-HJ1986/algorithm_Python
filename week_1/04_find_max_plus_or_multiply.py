def find_max_plus_or_multiply(array):
    max_num = 0;
    for num in array:
        if num <= 1 or max_num <= 1: #num이 1보다 작은 경우와 max_num이 1보다 작은 경우에는 더해줌.
            max_num += num
        else:
            max_num *= num
    return max_num


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))