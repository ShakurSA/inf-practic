from itertools import chain
from src.maps.base_map import BaseMap


class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(key={self.key}, value={self.val}"


class TreeMap(BaseMap):

    def __init__(self):
        self.root = None
        self.size = 0

    def __setitem__(self, key, val):
        def inner_setitem(node):
            if node is None:
                self.size += 1
                return TreeNode(key, val)
            else:
                if key == node.key:
                    node.val = val
                elif key < node.key:
                    node.left = inner_setitem(node.left)
                else:
                    node.right = inner_setitem(node.right)

                return node

        self.root = inner_setitem(self.root)

    def __getitem__(self, key):
        if self.root is None:
            raise KeyError
        node = self.root
        while node:
            if key < node.key:
                if node.left is None:
                    raise KeyError
                node = node.left
            elif key > node.key:
                if node.right is None:
                    raise KeyError
                node = node.right
            else:
                return node.val

    @staticmethod
    def find_min_node(node):
        if node.left is not None:
            return TreeMap.find_min_node(node.left)
        return node

    def __delitem__(self, key):
        '''
        recursive del
        '''
        def inner_delitem(node, key):
            if node is None:
                raise KeyError

            if key < node.key:
                node.left = inner_delitem(node.left, key)
                return node
            elif key > node.key:
                result = inner_delitem(node.right, key)
                node.right = result
                return node

            else:

                if node.left is None and node.right is None:
                    self.size -= 1
                    return None
                # есть только левый ребёнок
                elif node.left is not None and node.right is None:
                    self.size -= 1
                    return node.left
                # есть только правый ребёнок
                elif node.left is None and node.right is not None:
                    self.size -= 1
                    return node.right
                # есть оба ребёнка
                else:
                    min_node = TreeMap.find_min_node(node.right)
                    node.key = min_node.key
                    node.val = min_node.val
                    node.right = inner_delitem(node.right, min_node.key)

                    return node

        self.root = inner_delitem(self.root, key)

    def __str__(self):
        nodes = [self.root]
        lines = []
        while any(nodes):
            lines.append('\t'.join(str(node and node.key) for node in nodes))
            nodes = list(
                chain.from_iterable([node and node.left, node and node.right] for node in nodes)
            )
        return "\n".join(lines)



    def __contains__(self, item):
        def inner(node):
            if node is None:
                return False
            if node.key == item:
                return True
            if item < node.key:
                return inner(node.left)
            return inner(node.right)

        return inner(self.root)

    def __iter__(self):
        def iter_node(node):
            if node is not None:
                yield from iter_node(node.left)
                yield node.key, node.val
                yield from iter_node(node.right)

        yield from iter_node(self.root)

    def clear(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

