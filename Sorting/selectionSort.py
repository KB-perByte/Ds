def selectionSort(L):
    suffix = 0
    while suffix != len(L):
        for i in range(suffix , len(L)):
            if L[suffix] > L[i]:
                L[suffix], L[i] = L[i], L[suffix]
        suffix+=1
    return L

A = [3,2,3,4,5,6,7,83,23,54,3,23432,4]

print selectionSort(A)