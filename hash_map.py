class HashMap:
    class Node():
        def __init__(self,value = None,key = None ):
            self.value = value
            self.key = key
            self.next = None

    class Innerlinkedlist: # createlinkedlist
        def __init__(self):
            self.head = None
            self.end = None
            self.length = 0

        def insertatend(self,value, key): # Вставка в конец
            if self.head is None: # проверка на наличие листа
                self.head = self.end = HashMap.Node(value, key)
            else:
                self.end.next = self.end = HashMap.Node(value, key)
            self.length +=1

        def deletkey(self, key): # Удаление по ключу
            a = self.head
            if a.key == key: # проверка если он первый.
                self.head = a.next
                self.length-=1
            else: # идем и и сдвигаем
                while a.next:
                    if a.next.key == key:
                        a.next = a.next.next
                        self.length -=1
                        return
            return KeyError("Нет элемента с таким ключом")

        def __len__(self):
            return self.length

    def __init__(self, _size=10):
        self._inner_list = [None] *_size
        self._size = _size
        self._leng = 0

    def __getitem__(self, key):
        linked_list = self._inner_list[hash(key) % self._size]
        if linked_list is None: # проверка на наличие
            raise KeyError("Нет элемента, который подходит к ключу")
        a = linked_list.head # проходим по списку
        while a:
            if a.key == key:
                return a.value
            a = a.next
        raise KeyError("Нет элемента с таким ключом")

    def __setitem__(self, key, value):
        x = hash(key) % self._size # hash
        if self._inner_list[x] is None: # проверка на налчие
            self._inner_list[x] = HashMap.Innerlinkedlist() # list create
            self._inner_list[x].insertatend(value, key) # add
        else:
            a = self._inner_list[x]
            b = a.head
            while b:
                if b.key == key: # если ключе есть, то новое знач присваиваем
                    b.value = value
                    return
                b = b.next
            a.insertatend(value, key) # Если нет ключа, то добавить узел с этим значением и ключом
        self._leng += 1
        if self._leng >= (0.8 * self._size):
            self._size *=2
            new_list = [None] *self._size # Новый вдвое больше массив
            for i in self._inner_list: # проходит по всем спискам
                if i:
                    a = i.head
                    while a: # Проход по списку
                        x = hash(a.key) % self._size
                        if new_list[x] is None: # проверка на сущ листа с таким хешем, иначе создаем
                            new_list[x] = HashMap.Innerlinkedlist()
                            new_list[x].insertatend(a.value, a.key)
                        else: # иначе проходим и запис знач
                            b = new_list[x]
                            c = b.head
                            while c:
                                if c.key == key:
                                    c.value = value
                                    return
                                c = c.next
                            b.insertatend(value, key)
                        a = a.next
            self._inner_list = new_list # Перезаписываем новый в переменную старого

    def delete(self, key): # удаление эл из массива и уменьш массива
        for el in self._inner_list:
            if el: # если эл не пустой
                if len(el)>0: # проверка длины списка
                    el.deletkey(key)
        self._leng -=1
        if self._leng < self._size * 0.35 and self._size >0:
            self._size = self._size//2
            new_list = [None] * self._size  # Новый массив, вдвое больше
            for el in self._inner_list:
                if el:  # проверка на пустой спис
                    a = el.head
                    while a:  # Проход по списку
                        x = hash(a.key) % self._size
                        if new_list[x] is None:  # Если еще нет списка с таким значением хеша, то создаем
                            new_list[x] = HashMap.Innerlinkedlist()
                            new_list[x].insertatend(a.value, a.key)
                        else:  # В противном случае, на место элемента добавляем список с элемнтами
                            b = new_list[x]
                            b.insertatend(a.value, a.key)
                        a = a.next
            self._inner_list = new_list  # Перезаписываем новый в переменную старого списка

    def __len__(self):
        return self._size
