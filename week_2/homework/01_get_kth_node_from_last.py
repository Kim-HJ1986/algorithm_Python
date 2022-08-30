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

    def count_linked_list(self):
        count = 1
        cur = self.head
        while cur.next is not None:
            count += 1
            cur = cur.next

        return count

    def get_kth_node_from_last(self, k):
        all_count = self.count_linked_list()
        target_idx = all_count - k
        cur = self.head
        cur_idx = 0
        while cur.next is not None:
            if cur_idx == target_idx:
                return cur
            cur = cur.next
            cur_idx += 1
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(1)
linked_list.append(2)

print(linked_list.get_kth_node_from_last(4).data)  # 7이 나와야 합니다!
