def add(tree: tuple, value: int) -> tuple:
    if tree is None:
        tree = (value, None, None)
        return tree

    if value > tree[0]:
        return (tree[0], tree[1], add(tree[2], value))

    elif value <= tree[0]:
        return (tree[0], add(tree[1], value), tree[2])


def contains(tree: tuple, value: int) -> bool:
    if tree is None:
        return False

    if value > tree[0]:
        return contains(tree[2], value)

    if value == tree[0]:
        return True

    else:
        return contains(tree[1], value)


def tree_lenght(tree: tuple) -> int:
    if tree is None:
        return 0
    return max(tree_lenght(tree[1]), tree_lenght(tree[2]))+1

tree = (5, None, None)
print(tree_lenght(tree))
tree = add(tree, 2)

print(tree)
print(tree_lenght(tree))
print(contains(tree, 3))









