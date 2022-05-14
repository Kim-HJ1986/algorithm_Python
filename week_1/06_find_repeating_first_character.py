def find_not_repeating_first_character(string):
    all_list = []
    repeat_list = []
    for s in string:
        if s not in all_list:
            all_list.append(s)
        else:
            repeat_list.append(s)
    # 파이썬 배열간 뺄셈 한줄 표현!
    ans_list = [x for x in all_list if x not in repeat_list]

    # 파이썬 삼항 연산자
    return "_" if len(ans_list) == 0 else ans_list[0]

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))