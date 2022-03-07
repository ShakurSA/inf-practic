class HashMap:
    # class InnerLinkedList:
    #     pass

    def __init__(self, _size=10):
        self._inner_list = [(None, None)] * _size
        self._size = _size
        self._cnt = 0

    def __getitem__(self, key):
        return self._inner_list[hash(key) % self._size][1]

    def __setitem__(self, key, val):
        self._inner_list[hash(key) % self._size] = (key, val)
        self._cnt += 1
        if self._cnt >= 0.8 * self._size:
            self._size = self._size * 2
            new_inner_list = [(None, None)] * self._size
            for key, val in self._inner_list:
                new_inner_list[hash(key) % self._size] = (key, val)
            self._inner_list = new_inner_list

hash_map = HashMap()
hash_map[1] = 12
print(hash_map[1])
import random
for _ in range(100):
    p = random.randint(0, 100)
    q = random.randint(0, 100)
    hash_map[p] = q
    print(hash_map[p])