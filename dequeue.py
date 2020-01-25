from queue import CircularQueue
import unittest


class Dequeue(CircularQueue):
    def __init__(self, length):
        super().__init__(length)

    def add_first(self, item):
        if self.len >= self.max_size:
            raise Exception("Dequeue is full")
        self.zero_index -= 1
        if self.zero_index < 0:
            self.zero_index = self.max_size + self.zero_index
        self._queue[self.zero_index] = item
        self.len += 1

    def add_last(self, item):
        super().enqueue(item)

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

    def test_add(self):
        queue = Dequeue(20)
        for i in range(10):
            queue.add_last(i)
        for i in range(10, 20):
            queue.add_first(i)
        with self.assertRaises(Exception):
            queue.add_last(1)


if __name__ == "__main__":
    unittest.main()
