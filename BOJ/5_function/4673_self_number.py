def d(a):
    str_a = str(a)
    calc = a
    for i in range(len(str_a)):
        calc += int(str_a[i])
    return calc

all_list = list(range(1,10000))
minus_list = list()
for li in all_list:
    minus_list.append(d(li))

minus_set = set(minus_list)

# 차집합 한줄 코드
self_num_list = [x for x in all_list if x not in minus_set]

for r in self_num_list:
    print(r)