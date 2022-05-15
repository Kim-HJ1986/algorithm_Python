input = "000110011"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    sList = list(string)
    # 0과 1중 더 적은 값 구하기
    min_num = "1" if sList.count("0") >= sList.count("1") else "0"

    cnt=0
    for s in string:
        if s == min_num: # 만약 적은 값이라면 cnt += 1
            cnt+=1

    return cnt


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)