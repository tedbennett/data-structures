import unittest


class LinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self._next = next
            self._data = data

    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def add_first(self, data):
        new_first = self.Node(data)
        if self.len == 0:
            self.last = new_first
        else:
            new_first._next = self.first
        self.first = new_first
        self.len += 1

    def add_last(self, data):
        new_last = self.Node(data)
        if self.len == 0:
            self.first = new_last
        else:
            self.last._next = new_last
        self.last = new_last
        self.len += 1


class ListTest(unittest.TestCase):
    def test_list(self):
        """
        Testing adding and removing to the list
        :return:
        """
        linked = LinkedList()  # create empty list
        linked.add_last("1")
        linked.add_last("2")
        linked.add_first("3")
        item = linked.first
        for i in range(linked.len):
            print(item._data)
            item = item._next
        self.assertEqual(linked.remove_first(), "2")
        self.assertEqual(linked.remove_first(), "3")
        self.assertEqual(linked.remove_first(), "1")
        with self.assertRaises(IndexError):
            linked.remove_first()


if __name__ == "__main__":
    unittest.main()
