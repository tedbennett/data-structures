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
