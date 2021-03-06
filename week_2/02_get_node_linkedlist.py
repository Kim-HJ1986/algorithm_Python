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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur_index = 0
        cur_node = self.head
        while cur_index != index:
            cur_node = cur_node.next
            cur_index += 1
        return cur_node

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(9)
linked_list.append(3)

print(linked_list.get_node(0).data) # -> 5를 들고 있는 노드를 반환해야 합니다!