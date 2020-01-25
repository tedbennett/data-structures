from queue import CircularQueue
import unittest


class Dequeue(CircularQueue):
    def __init__(self):
        super().__init__()

    def add_first(self, item):
        if self.len >= self.max_size:
            raise Exception("Dequeue is full")
        self.zero_index -= 1
        if self.zero_index < 0:
            self.zero_index = self.max_size + self.zero_index
        self._queue[self.zero_index] = item
        self.len += 1

    def add_last(self, item):
        super().enqueue()

    def remove_first(self):
        super().dequeue()

    def remove_last(self):
        if self.len == 0:
            raise Exception("Dequeue is empty")
        index = (self.zero_index + self.len) % self.max_size  # finds end of queue, checks if needs to wrap around
        item = self._queue[index]
        self._queue[index] = None
        self.len -= 1
        return item

    def resize(self):
        super().resize()

    def first(self):
        super().first()

    def last(self):
        if self.len == 0:
            raise Exception("Queue is empty")
        return self._queue[self.zero_index + self.len]


    def is_empty(self):
        super().is_empty()

    def __len__(self):
        return super().__len__()


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

    def test_add(self):
        queue = Dequeue(20)
        for i in range(10):
            queue.add_last(i)
        for i in range(10, 20):
            queue.add_first(i)
        print(queue)
        with self.assertRaises(Exception):
            queue.add_last(1)

    def test_remove(self):
        queue = Dequeue(20)
        for i in range(10):
            queue.add_last(i)
        print(queue)
        self.assertEqual(len(queue), 10)
        self.assertEqual(queue.remove_first(), 0)
        self.assertEqual(len(queue), 9)
        self.assertEqual(queue.first(), 1)
        self.assertEqual(queue.remove_last(), 9)
        self.assertEqual(queue.last(), 8)
        print(queue)

    def test_wraparound(self):
        """
        Tests that adding extra elements will cause the queue to wraparound the array
        :return:
        """
        queue = CircularQueue(10)
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(queue.zero_index, 0)
        queue.dequeue()
        self.assertEqual(queue.zero_index, 1)
        queue.enqueue(11)  # should be at array index 0
        for i in range(8):
            queue.dequeue()
        self.assertEqual(queue.zero_index, 9)
        queue.dequeue()
        self.assertEqual(queue.zero_index, 0)
        self.assertEqual(queue.first(), 11)

    def test_resize(self):
        queue = CircularQueue(5)
        for i in range(5):
            queue.enqueue(i)
        queue.dequeue()
        self.assertEqual(queue.zero_index, 1)
        self.assertEqual(len(queue), 4)
        queue.resize(10)
        print(queue._queue)
        self.assertEqual(len(queue._queue), 10)
        self.assertEqual(queue.zero_index, 0)
        self.assertEqual(len(queue), 4)
        for i in range(4):
            queue.enqueue(i)
        with self.assertRaises(Exception):
            queue.resize(3)
