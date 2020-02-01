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

    def parent(self, p):
        node = self.check_position(p)
        return self.position(node.parent)

    def left(self, p):
        node = self.check_position(p)
        return self.position(node.left)

    def right(self, p):
        node = self.check_position(p)
        return self.position(node.right)

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

    def num_children(self, p):
        num = 0
        if self.right(p):
            num += 1
        if self.left(p):
            num += 1
        return num

    def delete(self, p):
        node = self.check_position(p)
        if self.num_children(p) > 1:
            raise ValueError("Position has 2 children")
        parent = node.parent
        if node.right:
            child = node.right
        else:
            child = node.left
        if child:
            child.parent = parent
        if not node.parent:  # node is root
            self._root = child
        else:
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child
        node.parent = node
        self.size -= 1
        return node.data

    def attach(self, p, left_tree, right_tree):
        node = self.check_position(p)
        if not self.is_leaf(p):
            raise ValueError("Position is not leaf")
        self.size += len(left_tree) + len(right_tree)
        if type(self) is type(left_tree) is type(right_tree):
            raise TypeError("Trees are not of correct type")
        if not left_tree.is_empty():
            node.left = left_tree._root
            node.left.parent = node.left
            left_tree._root = None
            left_tree.size = None
        if not right_tree.is_empty():
            node.right = right_tree._root
            node.right.parent = node.right
            right_tree._root = None
            right_tree.size = None

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
        children = [i for i in tree.children(left)]
        self.assertEqual(children, [child_left, child_right])
        self.assertEqual(tree.sibling(child_left), child_right)

    def test_delete(self):
        tree = BinaryTree()
        root = tree.add_root("root")
        left = tree.add_left(root, "left")
        child_left = tree.add_left(left, "left-left")
        child_right = tree.add_right(left, "left-right")
        with self.assertRaises(ValueError):
            tree.delete(left)
        self.assertEqual(tree.delete(child_left), "left-left")
        self.assertEqual(len(tree), 3)
        self.assertEqual(tree.delete(left), "left")
        left = tree.left(tree.root())
        self.assertEqual(tree.delete(root), "root")
        root = tree.root()
        self.assertEqual(tree.delete(root), "left-right")

        self.assertEqual(tree.is_empty(), True)
        self.assertEqual(len(tree), 0)

    def test_attach(self):
        tree1 = BinaryTree()
        root1 = tree1.add_root("root1")
        tree1.add_left(root1, "left1")

        tree2 = BinaryTree()
        root2 = tree2.add_root("root2")
        tree2.add_left(root2, "left2")
        tree2.add_right(root2, "right2")

        tree = BinaryTree()
        root = tree.add_root("root")

        tree.attach(root, tree1, tree2)
        self.assertEqual(len(tree), 6)
        children = [i for i in tree.children(root)]
        self.assertEqual(children, [root1, root2])






if __name__ == "__main__":
    unittest.main()
