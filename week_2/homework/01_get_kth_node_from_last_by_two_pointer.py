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

    # 두개의 노드 포인터를 통해 주어진 k만큼의 간격으로 답을 찾아간다.
    # 하지만 시간 복잡도 상의 장점은 없다.
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(1)
linked_list.append(2)

print(linked_list.get_kth_node_from_last(1).data)  # 7이 나와야 합니다!
