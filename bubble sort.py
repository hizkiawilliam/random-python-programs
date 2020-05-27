import random
import time
import psutil

L = []
for i in range(0,1000):
    L.append(random.randint(0,100))

def bubble(lst):
    for X in range(len(lst) - 1, 0, -1):
        for j in range(X):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
            
detik = time.time()
bubble(L)
detik2 = time.time()
print(detik2 - detik)
print(float(psutil.cpu_percent()))




#https://python-forum.io/Thread-bubble-sort-random-list
