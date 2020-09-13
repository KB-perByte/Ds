class Node:
    def __init__(self, data = None):
        super().__init__()
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self, _node):
        super().__init__(Node)
        self.listNode = _node
        self.head = None
    
    def insertL(self, data):
        if not self.head:
            self.head = data
        else:
            