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

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0: # index가 0일때 예외처리가 필요하다.
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        return

linked_list = LinkedList(5) # head 생성
linked_list.append(12) # next에 append 해주기
linked_list.append(9)
linked_list.append(3)

linked_list.add_node(2, 111)
linked_list.add_node(4, 222)
linked_list.add_node(6, 333)
linked_list.print_all()