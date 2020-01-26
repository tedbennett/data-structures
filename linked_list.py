import unittest


class LinkedListBase:
    class Node:
        def __init__(self, data=None, next=None):
            self.next = next
            self.data = data

    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def add_first(self, data):
        new_first = self.Node(data)
        if self.is_empty():
            self.last = new_first
        else:
            new_first.next = self.first
        self.first = new_first
        self.len += 1

    def add_last(self, data):
        new_last = self.Node(data)
        if self.is_empty():
            self.first = new_last
        else:
            self.last.next = new_last
        self.last = new_last
        self.len += 1

    def remove_first(self):
        if self.is_empty():
            raise IndexError
        new_first = self.first.next
        old_first = self.first

        self.first = new_first
        self.len -= 1
        if self.is_empty():
            self.last = None
        return old_first.data

    def is_empty(self):
        return self.len == 0

    def __len__(self):
        return self.len


class ListTest(unittest.TestCase):
    def test_list(self):
        """
        Testing adding and removing to the list
        :return:
        """
        linked = LinkedListBase()  # create empty list
        linked.add_last("1")
        linked.add_last("2")
        linked.add_first("3")
        item = linked.first
        self.assertEqual(linked.remove_first(), "3")
        self.assertEqual(linked.remove_first(), "1")
        self.assertEqual(linked.remove_first(), "2")
        with self.assertRaises(IndexError):
            linked.remove_first()


class LinkedStack(LinkedListBase):
    def __init__(self):
        super().__init__()

    def push(self, data):
        super().add_first(data)

    def pop(self):
        return super().remove_first()

    def top(self):
        if self.is_empty() and self.first is None:
            raise IndexError
        return self.first.data

    def __len__(self):
        return super().__len__()


class LinkedStackTest(unittest.TestCase):
    def test_stack(self):
        stack = LinkedStack()
        stack.push("1")
        stack.push("2")
        stack.push("3")
        self.assertEqual(stack.top(), "3")
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.pop(), "3")
        self.assertEqual(stack.pop(), "2")
        stack.pop()
        with self.assertRaises(IndexError):
            stack.pop()
        self.assertEqual(stack.is_empty(), True)


class LinkedQueueTest(unittest.TestCase):
    def test_queue(self):
        queue = LinkedQueue()
        queue.enqueue("1")
        queue.enqueue("2")
        queue.enqueue("3")
        self.assertEqual(queue.first(), "1")
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.dequeue(), "3")
        self.assertEqual(queue.dequeue(), "2")
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.dequeue()
        self.assertEqual(queue.is_empty(), True)





if __name__ == "__main__":
    unittest.main()
