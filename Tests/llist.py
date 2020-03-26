class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertEnd(self, key):
        if self.head == None:
            self.head = Node(key)
        else:
            temp = self.head
            while(temp):
                if temp.next == None:
                    temp.next = Node(key)
                    break
                temp = temp.next
            temp.next = Node(key)

    def insertBeg(self, key):
        if self.head != None:
            temp = self.head
            self.head = Node(key)
            self.head.next = temp
        else: 
            self.head = Node(key)

    def delItem(self, key):
        temp = self.head
        if self.head.next == None and self.head.data == key:
            self.head = None
            return
        elif self.head.data == key:
            self.head = temp.next
            temp = None
            return
        else:
            while(temp is not None):
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next
        if(temp==None):
            return
        prev.next = temp.next
        temp = None
                
    def printLList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        else:
            print("Empty! ")
        print('-----------------')

    def lenLList(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        return count

    def lPalin(self, head = None):
            head = self.head
            rev = None
            slow = fast = head
            #first, reverse the first half and find the middle
            while fast and fast.next:
                fast = fast.next.next
                rev, rev.next, slow = slow, rev, slow.next
            if fast:
                slow = slow.next
            #now compare the reversed first half with middle
            while rev and rev.data == slow.data:
                slow = slow.next
                rev = rev.next    
            return int(not rev)
        
if __name__ == '__main__':
    llobj =  LinkedList()

    llobj.printLList()

    llobj.insertBeg('one')
    llobj.insertEnd('two')
    llobj.insertEnd('three')
    llobj.insertBeg('zero')

    print(llobj.lenLList())

    llobj.printLList()
    llobj.insertBeg('minusone')
    llobj.insertEnd('four')
    llobj.printLList()

    print(llobj.lenLList())

    llobj.delItem('two')

    print(llobj.lenLList())
    print(llobj.lPalin(None))