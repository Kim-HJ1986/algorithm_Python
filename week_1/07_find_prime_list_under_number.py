import math

input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for i in range(2, number+1):
        if i == 2:
            prime_list.append(2)
        else:
            # 에라토스테네스의 체
            for j in range(2, math.ceil(i ** 0.5)+1):
                if i % j == 0:
                    break
                if j == math.ceil(i ** 0.5):
                    prime_list.append(i)


    return prime_list


result = find_prime_list_under_number(input)
print(result)