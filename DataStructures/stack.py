class Stack:
    '''LIFO implimentation of a list, i.e data can be accessed from the last not any othe place'''
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, _item):
        return self.items.append(_item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)