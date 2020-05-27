import time
import random

dataAmount = 1000
dataRange = 1000

List = [random.randint(0,dataRange) for i in range(0,dataAmount)]
    
def mergeSort(List):
    if len(List)>1:
        mid = len(List)//2
        lefthalf = List[:mid]
        righthalf = List[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                List[k]=lefthalf[i]
                i=i+1
            else:
                List[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            List[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            List[k]=righthalf[j]
            j=j+1
            k=k+1

start = time.time()
mergeSort(List)
end = time.time()
print(end - start)
input()
