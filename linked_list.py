import unittest


class Node:
    def __init__(self, data=None, next=None):
        self._node = next
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

    def test_list(self):
        node1 = Node("1")
        node2 = Node("2", node1)  # create list of 2 nodes, node2 pointing to node1
        self.assertEqual(node2.next(), node1)


if __name__ == "__main__":
    unittest.main()
