import unittest


class QueueBase:
    def __init__(self):
        self._queue = []
        self.len = 0
        self.zero_index = 0

    def enqueue(self, item):
        self._queue.append(item)
        self.len += 1

    def dequeue(self):
        if self.len == 0:
            raise Exception("Queue is empty")
        self.len -= 1
        item = self._queue[self.zero_index]
        self._queue[self.zero_index] = None
        self.zero_index += 1
        return item

    def first(self):
        if self.len == 0:
            raise Exception("Queue is empty")
        return self._queue[self.zero_index]

    def is_empty(self):
        return self.len == 0

    def __len__(self):
        return self.len


class CircularQueue(QueueBase):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size
        self._queue = [None] * self.max_size

    def enqueue(self, item):
        if self.len >= self.max_size:
            raise Exception("Queue is full")
        index = (self.zero_index + self.len) % self.max_size  # finds end of queue, checks if needs to wrap around
        self._queue[index] = item
        self.len += 1

    def dequeue(self):
        if self.len == 0:
            raise Exception("Queue is empty")
        self.len -= 1
        item = self._queue[self.zero_index]
        self._queue[self.zero_index] = None
        self.zero_index = (self.zero_index + 1) % self.max_size
        return item

    def first(self):
        return super().first()

    def is_empty(self):
        return super().is_empty()

    def __len__(self):
        return super().__len__()


class CircularQueueTest(unittest.TestCase):
    def test_init(self):
        """
        Tests queue initialises correctly, and checks first() raises and exception correctly
        :return:
        """
        queue = CircularQueue(20)
        self.assertEqual(queue.len, 0)
        self.assertEqual(len(queue._queue), 20)
        with self.assertRaises(Exception):
            queue.first()

    def test_enqueue(self):
        queue = CircularQueue(20)
        queue.enqueue("first")
        for i in range(19):
            queue.enqueue(i)
        with self.assertRaises(Exception):
            queue.enqueue(1)

    def test_dequeue(self):
        queue = CircularQueue(20)
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(len(queue), 10)
        self.assertEqual(queue.dequeue(), 0)
        self.assertEqual(len(queue), 9)
        self.assertEqual(queue.first(), 1)

    def test_wraparound(self):
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


if __name__ == "__main__":
    unittest.main()
