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
