import unittest
from linked_list import LinkedListBase


class DoublyLinkedList(LinkedListBase):
    def __init__(self):
        super().__init__()
        self.head_sentinel = self.Node()
        self.tail_sentinel = self.Node()
        self.head_sentinel.next = self.tail_sentinel
        self.head_sentinel.prev = None
        self.tail_sentinel.next = None
        self.tail_sentinel.prev = self.head_sentinel

    class Node(LinkedListBase.Node):
        def __init__(self):
            super().__init__()
            self.prev = None

    def add_first(self, data):
        new_node = self.Node()
        new_node.data = data
        old_node = self.head_sentinel.next
        new_node.next = old_node
        new_node.prev = self.head_sentinel
        old_node.prev = new_node
        self.head_sentinel.next = new_node
        self.len += 1

    def add_last(self, data):
        new_node = self.Node()
        new_node.data = data
        old_node = self.tail_sentinel.prev
        new_node.prev = old_node
        new_node.next = self.tail_sentinel
        old_node.next = new_node
        self.tail_sentinel.prev = new_node
        self.len += 1

    def remove_last(self):
        if self.is_empty():
            raise IndexError
        old_last = self.tail_sentinel.prev
        new_last = old_last.prev
        self.tail_sentinel.prev = new_last
        new_last.next = self.tail_sentinel
        self.len -= 1
        return old_last

    def remove_first(self):
        if self.is_empty():
            raise IndexError
        old_first = self.head_sentinel.next
        new_first = old_first.next
        self.head_sentinel.next = new_first
        new_first.prev = self.head_sentinel
        self.len -= 1
        return old_first

    def last(self):
        if self.is_empty():
            raise IndexError
        return self.tail_sentinel.prev


class DoublyLinkedTest(unittest.TestCase):
    def test_double(self):
        doubly_linked = DoublyLinkedList()
        doubly_linked.add_last("1")
        self.assertEqual(len(doubly_linked), 1)
        self.assertEqual(doubly_linked.last().data, "1")
        self.assertEqual(doubly_linked.remove_last().data, "1")
        self.assertEqual(doubly_linked.is_empty(), True)
        with self.assertRaises(IndexError):
            doubly_linked.remove_last()


if __name__ == "__main__":
    unittest.main()
