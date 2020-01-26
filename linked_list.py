import unittest


class DequeTest(unittest.TestCase):
    def test_node(self):
        node = Node()  # create empty node
        self.assertEqual(node.get_data(), None)  # check node data initialised correctly
        node.set_data("hello")
        self.assertEqual(node.get_data(), "hello")  # check set data
        self.assertEqual(node.next(), None)
