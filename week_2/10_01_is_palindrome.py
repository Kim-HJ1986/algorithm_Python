input = "토토"

# 반복문으로 회문 검사하기
def is_palindrome(string):
    result = True
    n = len(string)
    a = n // 2
    for i in range((n // 2) + 1):
        if string[i] != string[n - 1 - i]:
            result = False
    return result


print(is_palindrome(input))