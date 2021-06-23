def bubbleSortxas(A):
    lenA = len(A)
    flag = False
    while not flag :
        flag = True
        print A
        for j in range(1, lenA):
            print "---->",
            print A
            if A[j-1] > A[j]:
                flag = False
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    return A

A = [1, 54, 456, 343, 342,232,232,1,1,435,75]
B = [1,2,3,4,5]
C = [20,18,15,13,12]
D = [3,2,1]
#print bubbleSort(A)
print bubbleSortxas(B)
#print bubbleSort(C)
#print bubbleSort(D) 