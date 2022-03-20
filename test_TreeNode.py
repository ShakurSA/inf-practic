import unittest

from src.TreeNode import TreeNode


class SampleCase(unittest.TestCase):

    def setUp(self): # every test
        self.treemap = TreeNode()

    def test_treemap(self): # getitem
        self.treemap[10] = 'a'
        self.treemap[8] = 'b'
        self.treemap[5] = 'c'
        self.treemap[9] = 'd'
        self.treemap[7] = 'e'# Добавление элемента в дерево
        self.assertEquals(self.treemap[10],'a') # Подходит ли ключ 10 к value



if __name__=='__main__':
    unittest.main()