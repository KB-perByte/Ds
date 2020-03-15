def mergeSort(A):
    print "List situation : " + str(A)
    if len(A)<2:
        return A[:]
    else:
        middle = len(A) // 2
        leftA = mergeSort(A[:middle])
        rightA= mergeSort(A[middle:])
        return merge(leftA, rightA)

def merge(left , right):
    result = []
    
    i, j = 0,0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[i])
            j+=1
    while i< len(left):
        result.append(left[i])
        i+=1
    while j< len(right):
        result.append(right[j])
        j+=1
    return result


print mergeSort([89, 983, 34, 76,87,43,76,32,787,345,9870,2432,65768,9696,43,2,1,234,5445,74])