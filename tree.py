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
        self.size = 0

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
            return not (self == other)

    def check_position(self, p):
        """
        Positions won't necessarily refer to this particular container so must be validated
        :return:
        """
        if p.container is not self:
            raise ValueError("Position does not belong to this tree")
        if not isinstance(p, self.Position):
            raise TypeError("Must be Position type")
        if p.node.parent is p.node:  # when a node is deleted, its child takes its place
            raise ValueError("Deleted node")
        return p.node

    def position(self, node):
        if node is None:
            return None
        return self.Position(node, self)

    def root(self):
        return self.position(self._root)

    def add_root(self, data):
        node = self._Node(data)
        self._root = node
        self.size += 1
        return self.position(node)

    def add_left(self, p, data):
        node = self._Node(data)
        parent = self.check_position(p)
        parent.left = node
        node.parent = parent
        self.size += 1
        return self.position(node)

    def add_right(self, p, data):
        node = self._Node(data)
        parent = self.check_position(p)
        parent.right = node
        node.parent = parent
        self.size += 1
        return self.position(node)

    def left(self, p):
        node = self.check_position(p)
        return self.position(node.left)

    def right(self, p):
        node = self.check_position(p)
        return self.position(node.right)

    def children(self, p):
        return self.left(p), self.right(p)

    def num_children(self, p):
        num = 0
        if self.right(p):
            num += 1
        if self.left(p):
            num += 1
        return num

    def parent(self, p):
        node = self.check_position(p)
        return self.position(node.parent)

    def sibling(self, p):
        parent = self.parent(p)
        if self.check_position(parent):
            if self.left(parent) == p:
                return self.right(parent)
            return self.left(parent)
        return None

    def __len__(self):
        return self.size


class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree()
        with self.assertRaises(AttributeError):
            tree.add_left(tree.root(), "root")
        tree.add_root("root")
        root = tree.root()
        self.assertEqual(root.element(), "root")
        tree.add_left(root, "left")
        tree.add_right(root, "right")
        self.assertEqual(tree.left(root).element(), "left")
        self.assertEqual(tree.right(root).element(), "right")

    def test_size(self):
        tree = BinaryTree()
        root = tree.add_root("root")
        left = tree.add_left(root, "left")
        right = tree.add_right(root, "right")
        tree.add_left(left, "left-left")
        tree.add_right(left, "left-right")
        self.assertEqual(len(tree), 5)

    def test_children(self):
        # create a tree with a child with left and right children
        # check no. of children, if they're leaves and siblings
        tree = BinaryTree()
        root = tree.add_root("root")
        left = tree.add_left(root, "left")
        child_left = tree.add_left(left, "left-left")
        child_right = tree.add_right(left, "left-right")
        self.assertEqual(tree.num_children(left), 2)
        self.assertEqual(tree.is_leaf(left), False)
        self.assertEqual(tree.is_leaf(child_left), True)
        self.assertEqual(tree.children(left), (child_left, child_right))
        self.assertEqual(tree.sibling(child_left), child_right)


if __name__ == "__main__":
    unittest.main()
