class TreeNode:
    class Node:
        def __init__(self, key, value, left = None, right = None):
                self.key = key
                self.value = value
                self.left = left
                self.right = right
    def __init__(self):
        self.root = None

    def __getitem__(self, key):
        a = self.root
        if a is None:
            return None
        else:
            while a:
                if key > a.key:
                    if a.right is None:
                        return None
                    else:
                        a = a.right
                elif key < a.key:
                    if a.left is None:
                        return None
                    else:
                        a = a.left
                else:
                    return a.value





    def __setitem__(self, key, value):
        if self.root == None:
            self.root = TreeNode.Node(key,value)

        else:
            a = self.root
            while a.left is not None and a.right is not None:
                if key == a.key:
                    a.value = value
                    break
                elif key < a.key:
                    if a.left is None:
                        a.left = TreeNode.Node(key,value)
                        break
                    a = a.left

                elif key > a.key:
                    if a.right is None:
                        a.right = TreeNode.Node(key,value)
                        break
                    a.right = a.right



