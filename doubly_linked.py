import unittest
from linked_list import LinkedListBase


class DoublyLinkedList(LinkedListBase):
    def __init__(self):
        super().__init__()
        self.header = self.Node()
        self.trailer = self.Node()
        self.header.next = self.trailer
        self.header.prev = None
        self.trailer.next = None
        self.trailer.prev = self.header

    class Node(LinkedListBase.Node):
        def __init__(self):
            super().__init__()
            self.prev = None

    def add_first(self, data):
        new_node = self.Node()
        new_node.data = data
        old_node = self.header.next
        new_node.next = old_node
        new_node.prev = self.header
        old_node.prev = new_node
        self.header.next = new_node
        self.len += 1

    def add_last(self, data):
        new_node = self.Node()
        new_node.data = data
        old_node = self.trailer.prev
        new_node.prev = old_node
        new_node.next = self.trailer
        old_node.next = new_node
        self.trailer.prev = new_node
        self.len += 1

    def remove_last(self):
        if self.is_empty():
            raise IndexError
        old_last = self.trailer.prev
        new_last = old_last.prev
        self.trailer.prev = new_last
        new_last.next = self.trailer
        self.len -= 1
        return old_last

    def remove_first(self):
        if self.is_empty():
            raise IndexError
        old_first = self.header.next
        new_first = old_first.next
        self.header.next = new_first
        new_first.prev = self.header
        self.len -= 1
        return old_first

    def last(self):
        if self.is_empty():
            raise IndexError
        return self.trailer.prev


class DoublyLinkedTest(unittest.TestCase):
    def test_double(self):
        double_list = DoublyLinkedList()
        node1 = double_list.insert(double_list.header, double_list.trailer, "1")
        self.assertEqual(len(double_list), 1)
        self.assertEqual(double_list.last().data, "1")
        self.assertEqual(double_list.first().data, "1")

        node2 = double_list.insert(node1, double_list.trailer, "2")
        self.assertEqual(double_list.last(), node2)

        with self.assertRaises(IndexError):
            double_list.insert(double_list.header, double_list.trailer, "3")

        with self.assertRaises(IndexError):
            double_list.remove(double_list.header, double_list.trailer)

        self.assertEqual(double_list.remove(double_list.header, node2).data, "1")
        self.assertEqual(len(double_list), 1)
        self.assertEqual(double_list.remove(double_list.header, double_list.trailer).data, "2")
        with self.assertRaises(IndexError):
            double_list.remove(double_list.header, double_list.trailer)


if __name__ == "__main__":
    unittest.main()
