import unittest


class Node:
    def __init__(self, data=None):
        self._node = None
        self._data = data

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def next(self):
        return self._node


class NodeTest(unittest.TestCase):
    def test_node(self):
        node = Node()  # create empty node
        self.assertEqual(node.get_data(), None)  # check node data initialised correctly
        node.set_data("hello")
        self.assertEqual(node.get_data(), "hello")  # check set data
        self.assertEqual(node.next(), None)


if __name__ == "__main__":
    unittest.main()
