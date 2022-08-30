input = "토마ㅋ토"

# 반복문으로 회문 검사하기
def is_palindrome(string):
    result = True
    len_of_string = len(string)
    mid_index = len_of_string // 2
    for i in range(mid_index + 1):
        if string[i] != string[len_of_string - 1 - i]:
            result = False
    return result


print(is_palindrome(input))
