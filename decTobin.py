from stack import Stack

def decToBinary(i):
    s = Stack()
    while i > 0:
        s.push(i % 2)
        i//=2

    binString = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString

print decToBinary(2354)
print bin(2354)
print bin(2) is decToBinary(2)
print bin(2) == decToBinary(2)

#the reverse \m/
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))
