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


