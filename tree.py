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


class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree()
        tree.add_root("root")
        root = tree.root()
        self.assertEqual(root.element(), "root")
        tree.add_left(root, "left")
        tree.add_right(root, "right")
        self.assertEqual(tree.left(root), "left")
        self.assertEqual(tree.right(root), "right")
