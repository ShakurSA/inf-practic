import copy

class Num:
    class Node:
        def __init__(self, next = None, value = None , prev= None , sign = 1):
            self.next = next
            self.value = value
            self.prev = prev
            if sign == None:
                if value < 0:
                    self.sign = -1
                else:
                    self.sign = 1
            else:
                self.sign = sign

        def __add__(self, other):
            if isinstance(other, Num.Node):
                return self.value * self.sign + other.value * other.sign

    def __init__(self, number = 0):
        if number < 0:
            self.sign = -1
            number = -number
        else:
            self.sign = 1

        self.head = Num.Node(sign = self.sign)
        self.tail = Num.Node(sign = self.sign)

        curr = None
        self.tail = Num.Node(value=number % 10, sign = self.sign)
        curr = self.tail
        number = number // 10

        while number > 0:
            new_node = Num.Node(next=curr, value=number % 10, sign = self.sign)
            curr.prev = new_node
            curr = new_node
            number = number // 10
        self.head = curr

    def __neg__(self):
        new_num = copy.deepcopy(self)
        new_num.sign = new_num.sign
        curr = new_num.head
        while curr.next != None:
            curr.sign = new_num.sign * (-1)

        return new_num

    def __add__(self, other):
        new_number = Num()
        curr1 = self.tail
        curr2 = other.tail
        new_number.tail.value = curr1 + curr2
        curr = new_number.tail
        yy = curr.value // 10
        curr.value %= 10
        null_node = Num.Node(value = 0)

        while curr1.prev != None or curr2.prev != None:
            if curr1.prev != None:
                curr1 = curr1.prev
            else:
                curr1 = null_node

            if curr2.prev != None:
                curr2 = curr2.prev
            else:
                curr2 = null_node


            new_node = Num.Node(next= curr, value=curr1+curr2+yy)

            yy = curr.value // 10
            curr.value  %= 10
            curr.prev = new_node
            curr = new_node

        if yy != 0:
            new_node = Num.Node(next =curr, value=yy)
            curr.prev = new_node
            curr = new_node

        new_number.head = curr
        return new_number

    def __sub__(self, other):
        return self + other *(-1)

    def __str__(self):
        s = ''
        if self.sign == -1:
            s = '-'
        curr = self.head
        while curr.next != None:
            s += str(curr)
            curr = curr.next
        s += str(curr)
        return s


    def __repr__(self):
        return str(self)



chis_1 = Num(243234)
chis_2 = Num(34)
chis_2_neg = - chis_2
chis_4 = chis_1 - chis_2
print(chis_1)

print(chis_4)









