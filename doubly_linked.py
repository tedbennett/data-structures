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

    def clear(self):
        for i in range(self.len):
            item_to_remove = self.header.next
            assert(item_to_remove != self.trailer)
            self.remove(self.header, item_to_remove.next)


class DoublyLinkedTest(unittest.TestCase):
    def test_double(self):
        """
        Test to check items are correctly inserted into the DL list.
        :return:
        """
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

    def test_clear(self):
        """
        Test to ensure clear() correctly clears a list
        :return:
        """
        double_list = DoublyLinkedList()
        next_node = double_list.insert(double_list.header, double_list.trailer, 0)
        for i in range(1, 6):
            next_node = double_list.insert(next_node, double_list.trailer, i)
        self.assertEqual(len(double_list), 6)
        double_list.clear()
        self.assertEqual(double_list.is_empty(), True)
        with self.assertRaises(IndexError):
            double_list.remove(double_list.header, double_list.trailer)


class PositionalTest(unittest.TestCase):
    def test_access(self):
        """
        Positional list introduces a wrapper class for nodes, the Position
        :return:
        """
        position_list = PositionalList()
        for i in range(5):
            position_list.add_last(i)
        p = position_list.first()
        self.assertEqual(p.element().data, 0)
        for i in range(1, 5):
            p = position_list.after(p)
            self.assertEqual(p.element().data, i)



if __name__ == "__main__":
    unittest.main()
