from stack import Stack
#stack is beautiful
mystack = Stack()
herstack = Stack()
mystack.push(1)
mystack.push(9)
mystack.push(9)
mystack.push(6)
mystack.push('Sagar')
print mystack.size()
print mystack.peek()
mystack.pop()
print mystack.size()
print mystack.isEmpty()
print herstack.isEmpty()
herstack = mystack
print herstack == mystack
print id(herstack) 
print id(mystack)
herstack.push('Nandini')
print herstack.peek()
print id(herstack)
print id(mystack)
print mystack.peek()
print herstack.size()