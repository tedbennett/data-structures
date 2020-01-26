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
        data = remove_node.data
        remove_node.next = remove_node.prev = remove_node.data = None
        return data

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

        self.assertEqual(double_list.remove(double_list.header, node2), "1")
        self.assertEqual(len(double_list), 1)
        self.assertEqual(double_list.remove(double_list.header, double_list.trailer), "2")
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


class PositionalList(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    class Position:
        def __init__(self, node, container):
            self.node = node
            self.container = container

        def element(self):
            return self.node.data

        def __eq__(self, other):
            return type(other) is type(self) and self.node is other.node

        def __ne__(self, other):
            return not(self == other)

    def check_position(self, p):
        """
        Positions won't necessarily refer to this particular container so must be validated
        :return:
        """
        if p.container is not self:
            raise ValueError
        if not isinstance(p, self.Position):
            raise TypeError
        if p.node.next is None:
            raise ValueError
        return p.node

    def position(self, node):
        if node is self.trailer or node is self.header:
            return None
        return self.Position(node, self)

    def insert_before(self, p, data):
        end_node = self.check_position(p)
        begin_node = end_node.prev
        node = super().insert(begin_node, end_node, data)
        return self.position(node)

    def insert_after(self, p, data):
        begin_node = self.check_position(p)
        end_node = begin_node.next
        node = super().insert(begin_node, end_node, data)
        return self.position(node)

    def add_first(self, data):
        node = self.insert(self.header, self.header.next, data)
        return self.position(node)

    def add_last(self, data):
        self.insert(self.trailer.prev, self.trailer, data)

    def before(self, p):
        node = self.check_position(p)
        return self.position(node.prev)

    def after(self, p):
        node = self.check_position(p)
        return self.position(node.next)

    def replace(self, p, data):
        node = self.check_position(p)
        node.data = data
        return self.position(node)

    def delete(self, p):
        node = self.check_position(p)
        next_node = node.next
        prev_node = node.prev
        return super().remove(prev_node, next_node)

    def first(self):
        return self.position(self.header.next)

    def last(self):
        return self.position(self.trailer.prev)

    def __iter__(self):
        current = self.first()
        while current is not None:
            yield current.element()
            current = self.after(current)


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
        self.assertEqual(p.element(), 0)
        for i in range(1, 5):
            p = position_list.after(p)
            self.assertEqual(p.element(), i)

    def test_iter(self):
        position_list = PositionalList()
        for i in range(5):
            position_list.add_last(i)

        for idx, item in enumerate(position_list):
            self.assertEqual(item, idx)

    def test_delete(self):
        position_list = PositionalList()
        for i in range(5):
            position_list.add_last(i)
        p = position_list.first()
        p = position_list.after(p)
        self.assertEqual(position_list.delete(p), 1)
        p = position_list.last()
        p = position_list.before(p)
        self.assertEqual(position_list.delete(p), 3)
        for idx, item in enumerate(position_list):  # should be 0, 2, 4
            self.assertEqual(item, 2 * idx)
        for i in range(3):
            p = position_list.first()
            position_list.delete(p)
        with self.assertRaises(ValueError):  # Expired position
            position_list.delete(p)


if __name__ == "__main__":
    unittest.main()
