from random import *


class node:

    def __init__(self, num):
        self.body = num
        self.next = None


class linked_list:

    def __init__(self):
        self.head = node(None)
        self.c_node = self.head

    def append(self, new_node):
        self.c_node.next = new_node
        self.c_node = new_node

    def show_all(self):
        if self.c_node.body is None:
            print('list is empty')
            return

        while True:
            node1 = self.head.next

            if node1 is None:
                break

            print(node1.body, end='')


ll = linked_list()

for i in range(1, 10):
    ll.append(node(randint(1, 23)))

ll.show_all()
