import unittest

from src.maps.hash_map import HashMap

class SampleCase(unittest.TestCase):

    def setUp(self): # every test
        self.hm = HashMap()

    def test_hash_map(self): # getitem
        self.hm["ab"] = 1
        self.assertEquals(self.hm["ab"], 1) # Проверка является ключ ad к 1

    def test_delkey(self): # delete
        self.hm["ab"] = 1
        del self.hm["ab"] # Удаление элемента
        self.assertRaises(KeyError, lambda: self.hm["ab"]) # если ключа нет

    def test_size(self): # size up
        for i in range(5): # часть массива заполняем
            self.hm[i] = i
        leng1 = len(self.hm) # len
        self.hm[5] = 5
        leng2 = len(self.hm) # len after
        self.assertTrue(leng1<leng2) # len < lenafter

    def test_min_size(self):# проверка на уменьшение
        for i in range(7):
            self.hm[i] = i
        leng1 = len(self.hm)# len
        del self.hm[3]
        leng2 = len(self.hm)# lenafter
        self.assertTrue(leng1>leng2)# len > lenafter

    def test_eq_key(self): # Проверка на то, что значение по ключу заменяется при повторе
        self.hm["key"] = 1
        self.hm["key"] = 2
        self.assertEquals(self.hm["key"], 2) # Проверка на то, что по ключу "key" будет последнее значение 2

if __name__=='__main__':
    unittest.main()