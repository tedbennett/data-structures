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
            self.next = None
            self.prev = None

    def insert(self, begin, end, data):
        if begin.next != end or end.prev != begin:
            raise IndexError
        new_node = self.Node()
        new_node.data = data
        new_node.next = end
        new_node.prev = begin
        begin.next = new_node
        end.prev = new_node
        self.len += 1
        return new_node

    def remove(self, begin, end):
        remove_node = begin.next
        if remove_node.next != end:
            raise IndexError
        begin.next = end
        end.prev = begin
        self.len -= 1
        return remove_node

    def first(self):
        if self.is_empty():
            raise IndexError
        return self.header.next

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
