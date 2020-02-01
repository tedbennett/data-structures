import unittest


class TreeBase:
    """
    Abstract base class
    """

    class Position:
        def element(self):
            raise NotImplementedError

        def __eq__(self, other):
            raise NotImplementedError

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError

    def is_root(self, p):
        return self.root() == p

    def parent(self, p):
        raise NotImplementedError

    def num_children(self, p):
        raise NotImplementedError

    def children(self, p):
        raise NotImplementedError

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def __len__(self):
        raise NotImplementedError

    def is_empty(self):
        return len(self) == 0

    def positions(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError


class BinaryTreeBase(TreeBase):
    def __init__(self):
        super().__init__()

    def left(self, p):
        raise NotImplementedError

    def right(self, p):
        raise NotImplementedError

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        # iterator
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class BinaryTree(BinaryTreeBase):
    def __init__(self):
        super().__init__()
        self._root = None

    class _Node:
        def __init__(self, data, left=None, right=None, parent=None):
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent

    class Position:
        def __init__(self, node, container):
            self.node = node
            self.container = container

        def element(self):
            return self.node.data

        def __eq__(self, other):
            return type(other) is type(self) and self.node is other.node

        def __ne__(self, other):
            return not(self == other)

    def root(self):
        return self.Position(self._root, self)

    def add_root(self, data):
        node = self._Node(data)
        self._root = node

    def add_left(self, p, data):
        node = self._Node(data)
        p.node.left = node

    def add_right(self, p, data):
        node = self._Node(data)
        p.node.right = node

    def left(self, p):
        return self.Position(p.node.left, self)

    def right(self, p):
        return self.Position(p.node.right, self)


class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree()
        tree.add_root("root")
        root = tree.root()
        self.assertEqual(root.element(), "root")
        tree.add_left(root, "left")
        tree.add_right(root, "right")
        self.assertEqual(tree.left(root).element(), "left")
        self.assertEqual(tree.right(root).element(), "right")


if __name__ == "__main__":
    unittest.main()
