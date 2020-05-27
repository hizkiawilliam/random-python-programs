import math

def move(a):
    if(a==1):
        return 1
    else:
        return 2*(move(a-1))

print(move(16))
