'''recursion is a process of doing a similar task by reusing the code for similar task . '''
'''recursion must not be infinite loop'''



def mul(a , b):
    r = 0
    while b > 0:
        r+=a
        b-=1 
    return r

def mulrec(a,b):
    if b == 1:
        return a
    else:
        return a + mulrec(a, b-1)

print mulrec(2,10)
print mul(2,10)