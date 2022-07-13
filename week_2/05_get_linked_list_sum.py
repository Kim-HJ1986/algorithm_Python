class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def return_str(self):
    strVal=""
    node = self.head
    while True:
        strVal += str(node.data)
        node = node.next
        if node is None:
            break
    return strVal

def get_linked_list_sum(linked_list_1, linked_list_2):
    list_sum_1 = return_str(linked_list_1)
    list_sum_2 = return_str(linked_list_2)
    sum = int(list_sum_1) + int(list_sum_2)
    return sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))