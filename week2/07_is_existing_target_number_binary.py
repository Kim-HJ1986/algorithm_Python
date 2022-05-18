finding_target = 7
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 위와 같이 정렬이 되지 않은 무작위 배열은 이진탐색이 불가능하다.
# 따라서 이진 탐색을 하기 위해선 먼저 배열을 일정한 규칙으로 정렬해야 한다.
def is_exist_target_number_binary(target, numbers):
    # 정렬 내장 함수 사용
    numbers.sort()
    min_idx = 0
    max_idx = len(numbers) - 1
    cur_idx = (min_idx + max_idx) // 2

    while min_idx <= max_idx:
        if numbers[cur_idx] == target:
            return True
        elif numbers[cur_idx] > target:
            max_idx = cur_idx - 1
        elif numbers[cur_idx] < target:
            min_idx = cur_idx + 1
        cur_idx = (min_idx + max_idx) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)