shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "떡이"]


# 시간 복잡도는 O( (M + N) * logN )
def is_available_to_order(menus, orders):

    # sort()의 시간 복잡도는 N * logN 이다.
    menus.sort()
    orders.sort()

    # 아래 반복문 전체 시간 복잡도는 M * logN
    for order in orders: # 반복 횟수 M
        if not is_include(order, menus): # 이분탐색 logN
            return False
    return True


# 이분 탐색으로 정렬된 배열에서 타겟 찾기
def is_include(target, array):
    first = 0
    last = len(array) - 1
    target_idx = (first + last) // 2

    while first <= last:
        if array[target_idx] == target:
            return True
        elif array[target_idx] < target:
            first = target_idx + 1
        else:
            last = target_idx - 1
        target_idx = (first + last) // 2
    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)
