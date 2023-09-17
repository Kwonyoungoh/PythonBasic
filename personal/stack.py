class Stack:

    def __init__(self):
        self.lst = []

    def add(self, num):
        self.lst.append(num)

    def pop(self):
        if not self.lst:
            print('Stack is empty')
            return None
        return self.lst.pop()

    def show(self):
        print(self.lst)


s1 = Stack()
s1.add(2)
s1.add(3)
s1.add(45)

s1.show()

s1.pop()

s1.show()
