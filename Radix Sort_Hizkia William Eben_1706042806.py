import time
import random

dataAmount = 1000
dataRange = 1000

List = [random.randint(0,dataRange) for i in range(0,dataAmount)]

def radixSort( List ):
  RADIX = len(List)
  maxLength = False
  tmp , placement = -1, 1
  while not maxLength:
    maxLength = True
    buckets = [list() for _ in range( RADIX )]
    for  i in List:
      tmp = i / placement
      buckets[int(tmp % RADIX)].append(int(i))
      if maxLength and tmp > 0:
        maxLength = False
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        List[a] = i
        a += 1
    placement *= RADIX 

start = time.time()
radixSort(List)
end = time.time()
print(end - start)
input()
