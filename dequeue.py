from queue import CircularQueue
import unittest


class Deque(CircularQueue):
    def __init__(self, length):
        super().__init__(length)

    def add_first(self, item):
        if self.len >= self.max_size:
            raise Exception("Deque is full")
        self.zero_index -= 1
        if self.zero_index < 0:
            self.zero_index = self.max_size + self.zero_index
        self._queue[self.zero_index] = item
        self.len += 1

    def add_last(self, item):
        super().enqueue(item)

    def remove_first(self):
        return super().dequeue()

    def remove_last(self):
        if self.len == 0:
            raise Exception("Dequeue is empty")
        index = (self.zero_index + self.len - 1) % self.max_size  # finds end of queue, checks if needs to wrap around        print(self.zero_index)
        item = self._queue[index]
        self._queue[index] = None
        self.len -= 1
        return item

    def first(self):
        return super().first()

    def last(self):
        if self.len == 0:
            raise Exception("Deque is empty")
        return self._queue[self.zero_index + self.len - 1]


class DequeTest(unittest.TestCase):
    def test_init(self):
        """
        Tests deque initialises correctly, and checks first() raises and exception correctly
        :return:
        """
        queue = Deque(20)
        self.assertEqual(queue.len, 0)
        self.assertEqual(len(queue._queue), 20)
        with self.assertRaises(Exception):
            queue.first()
        with self.assertRaises(Exception):
            queue.last()

    def test_add(self):
        queue = Deque(20)
        for i in range(10):
            queue.add_last(i)
        for i in range(10, 20):
            queue.add_first(i)
        with self.assertRaises(Exception):
            queue.add_last(1)

    def test_remove(self):
        queue = Deque(20)
        for i in range(10):
            queue.add_last(i)
        self.assertEqual(len(queue), 10)
        self.assertEqual(queue.remove_first(), 0)
        self.assertEqual(len(queue), 9)
        self.assertEqual(queue.first(), 1)
        self.assertEqual(queue.remove_last(), 9)
        self.assertEqual(queue.last(), 8)


if __name__ == "__main__":
    unittest.main()
