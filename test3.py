import random

def maximum(A):
    big = 0
    for i in range(0,len(A)):
        if A[i] > big:
            big = A[i]
    return big

A = []
for i in range(0,10-1):
    A.append(1)
    A[i] = random.randrange(1,10000)
print(A)
print(maximum(A))

#1 + n-1(2)
#1 + 2n-2
#2n-1
#big O = O(n)
