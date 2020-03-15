def searchMatrix(A, B):
        N = len(A) #rows
        #M = len(A[0]) #columns
        suspectRow = []
        if N > 1:
            for i in A:
                if B <= max(i):
                    suspectRow.append(i)
                    break
                elif B > max(i):
                    continue
                else:
                    return 0
        else: 
            suspectRow.append(A)
        for m in suspectRow[0]:
            if B == m:
                return 1
            

A = [  [3, 3, 11, 12, 14],
  [16, 17, 30, 34, 35],
  [45, 48, 49, 50, 52],
  [56, 59, 63, 63, 65],
  [67, 71, 72, 73, 79],
  [80, 84, 85, 85, 88],
  [88, 91, 92, 93, 94] ]
B = 94

print searchMatrix(A, B)