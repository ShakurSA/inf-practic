class HashMap:
    class Node():
        def __init__(self,value = None,key = None ):
            self.value = value
            self.key = key
            self.next = None

        def __iter__(self):
            yield self.key, self.value

            if self.next is not None:
                yield from self.next


    class Innerlinkedlist:
        def __init__(self):
            self.head = None
            self.end = None
            self.length = 0

        def insert_at_end(self,value, key):
            '''
            add
            '''
            if self.head is None:
                self.head = self.end = HashMap.Node(value, key)
            else:
                self.end.next = self.end = HashMap.Node(value, key)
            self.length += 1

        def delete_key(self, key): # Удаление по ключу
            '''
            delete
            '''
            a = self.head
            if self.head is None:
                return
            if a.key == key: # проверка если он первый.
                self.head = a.next
            else:
                while a.next:
                    if a.next.key == key:
                        a.next = a.next.next
                        self.length -=1
                        break

        def __len__(self):
            return self.length

        def __iter__(self):
            if self.head is not None:
                yield from self.head



    def __init__(self, _size=10):
        self._inner_list = [None] *_size
        self._size = _size
        self._leng = 0

    def __iter__(self):
        for linked_list in self._inner_list:
            yield from linked_list or []

    def __getitem__(self, key):
        linked_list = self._inner_list[hash(key) % self._size]
        if linked_list is None:
            raise KeyError
        a = linked_list.head
        while a:
            if a.key == key:
                return a.value
            a = a.next
        raise KeyError

    def __setitem__(self, key, value):
        x = hash(key) % self._size # hash
        if self._inner_list[x] is None: # проверка на налчие
            self._inner_list[x] = HashMap.Innerlinkedlist() # list create
            self._inner_list[x].insert_at_end(value, key) # add
        else:
            a = self._inner_list[x]
            b = a.head
            while b:
                if b.key == key: # если ключ есть, то новое знач присваиваем
                    b.value = value
                    return
                b = b.next
            a.insert_at_end(value, key) # Если нет ключа, то добавить узел с этим значением и ключом
        self._leng += 1
        if self._leng >= (0.8 * self._size):
            self._size = self._size * 17 // 10
            new_list = [None] *self._size # Новый вдвое больше массив
            for i in self._inner_list: # проходит по всем спискам
                if i:
                    curr = i.head
                    while curr: # Проход по списку
                        index = hash(curr.key) % self._size
                        if new_list[index] is None: # проверка на сущ листа с таким хешем, иначе создаем
                            new_list[index] = HashMap.Innerlinkedlist()
                            new_list[index].insert_at_end(curr.value, curr.key)
                        else: # иначе проходим и запис знач
                            b = new_list[index]
                            b.insert_at_end(curr.key, curr.value)
                        curr = curr.next
            self._inner_list = new_list # Перезаписываем новый в переменную старого

    def __delitem__(self, key):
        for linked_list in self._inner_list:
            if linked_list is not None:
                linked_list.delete_key(key)
        self._leng -= 1
        if self._leng < self._size * 0.8 and self._size > 10:
            self._size = self._size// 17*10
            new_list = [None] * self._size
            for el in self._inner_list:
                if el:
                    a = linked_list.head
                    while a:
                        x = hash(a.key) % self._size
                        if new_list[x] is None:
                            new_list[x] = HashMap.Innerlinkedlist()
                            new_list[x].insert_at_end(a.value, a.key)
                        else:
                            b = new_list[x]
                            b.insert_at_end(a.value, a.key)
                        a = a.next
            self._inner_list = new_list



    def __len__(self):
        return self._leng

    def __contains__(self, item):
        for list in self._inner_list:
            if list is not None:
                for elem in list:
                    if elem[0] == item:
                        return True
        return False

    def __str__(self) -> str:
        return '[' + ', '.join(map(str, self._inner_list)) + ']'

    def clear(self) -> None:
        self._size = 10
        self._inner_list = [None] * self._size
        self._leng = 0
