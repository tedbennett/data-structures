import unittest



class CircularListTest(unittest.TestCase):
    def test_list(self):
        """
        Testing adding and removing to the list
        :return:
        """
        linked = CircularList()  # create empty list
        linked.add_last("1")
        linked.add_last("2")
        linked.add_first("3")
        self.assertEqual(linked.remove_first(), "3")
        self.assertEqual(linked.remove_first(), "1")
        self.assertEqual(linked.remove_first(), "2")
        with self.assertRaises(IndexError):
            linked.remove_first()
