import random
import time


def bucketSort(seq):
    biggest = 0
    for number in seq:
        if number > biggest:
            biggest = number
    buckets = []
    buckets.append([]) * (biggest / 10 + 1)
    for number in seq:
        buckets[number / 10].append(number)
    for index, bucket in enumerate(buckets):
        #Using quicksort to sort individual buckets
        buckets[index] = quicksort(bucket)
    new_list = [number for number in bucket for bucket in buckets]
    return new_list
L = []
for i in range(0,10000):
    L.append(random.randint(0,1000))

detik = time.time()
bucketSort(L)
detik2 = time.time()
print(detik2 - detik)
