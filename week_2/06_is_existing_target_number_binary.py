finding_target = 16
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 이진 탐색 (binary search) 시간복잡도 -> O(lonN)
def is_existing_target_number_binary(target, array):
    cur_min_idx = 0
    cur_max_idx = len(array) - 1
    cur_guess_idx = (cur_max_idx + cur_min_idx) // 2
    find_count = 0

    while cur_min_idx <= cur_max_idx:
        find_count += 1
        if array[cur_guess_idx] == target:
            print(find_count)
            return True
        elif array[cur_guess_idx] < target:
            cur_min_idx = cur_guess_idx + 1
        else:
            cur_max_idx = cur_guess_idx - 1
        cur_guess_idx = (cur_max_idx + cur_min_idx) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)