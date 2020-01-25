from queue import CircularQueue
import unittest


class Dequeue(CircularQueue):
    def __init__(self, length):
        super().__init__(length)

    def first(self):
        super().first()

    def last(self):
        if self.len == 0:
            raise Exception("Queue is empty")
        return self._queue[self.zero_index + self.len]


class DequeueTest(unittest.TestCase):
    def test_init(self):
        """
        Tests dequeue initialises correctly, and checks first() raises and exception correctly
        :return:
        """
        queue = Dequeue(20)
        self.assertEqual(queue.len, 0)
        self.assertEqual(len(queue._queue), 20)
        with self.assertRaises(Exception):
            queue.first()
        with self.assertRaises(Exception):
            queue.last()


if __name__ == "__main__":
    unittest.main()
