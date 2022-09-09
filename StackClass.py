from NodeClass import Node

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top, out))

    __repr__ = __str__

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def __len__(self):
        temp = self.top
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def push(self, value):
        new_node = Node(value)
        temp = self.top
        if self.isEmpty() == True:
            self.top = new_node
            self.top.next = None
        else:
            self.top = new_node
            self.top.next = temp

    def pop(self):
        temp = self.top
        if self.isEmpty() == True:
            return None
        else:
            self.top = self.top.next
            return temp.value


    def peek(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.top.value
