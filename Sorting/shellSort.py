def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        
        print("After increment fo size", sublistcount, "The list is ", alist)

        sublistcount = sublistcount//2

def gapInsertionSort(alist, start, gap):
    for i in range( start+gap, len(alist), gap):
        currentValue = alist(i)
        posittion = i
    
    while posittion >= gap and alist[posittion -  gap] >  currentValue:
        alist[posittion] = alist[posittion-gap]
        posittion = posittion - gap

    alist[posittion] = currentValue


alist = [2313,23,2,32,3,4,453,65,7,6,6,74,5,23,4,37,57,4,5,7645,7,62]

shellSort(alist)
print(alist)

