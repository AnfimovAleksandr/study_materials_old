import pickle

class Node:
    def __init__(self):
        self.next = None
        self.data = None
    def __init__(self, data):
        self.next = None
        self.data = data
    def append(self, val):
        if self.data == None:
            self.data = val
        else:
            end = Node(val)
            n = self
            while (n.next):
                n = n.next
            n.next = end
    def delete(self, n):
        if self.data == None:
            print('Нечего удалять')
        else:
            last = self
            now = last.next
            if n == 0:
                self.data = now
            else:
                flag = 0
                while n > 1:
                    n -= 1
                    if now == None:
                        print('Такой ячейки не существует')
                        flag = 1
                    last = now
                    now = last.next
                last.next = now.next
    def ndump(self):
        with open('./data.pickle', 'wb') as f:
            pickle.dump(self, f , pickle.HIGHEST_PROTOCOL)
    def __str__(self):
        out = ''
        if self.data == None:
            out += 'Список пуст'
        else:
            n = self
            while (n.next):
                out += str(n.data)
                out += ' '
                n = n.next
            out += 'Конец списка'
        return out


Spisok = Node(0)
for i in range(1, 10):
    Spisok.append(i)
print(Spisok)

data = Spisok.ndump()
with open("./data.pickle", "rb") as f:
    Copy = pickle.load(f)

print(Copy)

