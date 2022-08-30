shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "떡볶이"]


# 시간 복잡도는 O(M + N)
def is_available_to_order(menus, orders):

    # set()의 시간 복잡도는 O(N) 이다.
    menus_set = set(menus)

    # 아래 반복문 전체 시간 복잡도는 O(M)
    for order in orders: # 반복 횟수 M
        if order not in menus_set: # set 자료 탐색 O(1)
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
