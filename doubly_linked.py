import unittest


class DoubleTest(unittest.TestCase):
    def double_test(self):
        doubly_linked = DoublyLinkedList()
        doubly_linked.add_last("1")
        self.assertEqual(len(doubly_linked), 1)
        self.assertEqual(doubly_linked.last(), "1")
        self.assertEqual(doubly_linked.remove_last(), "1")
        self.assertRaises(doubly_linked.is_empty(), True)
        with self.assertRaises(IndexError):
            doubly_linked.remove_last()
