def sm(x, y, n):
    if n == 0:
        return x
    else:
        return y + sm(x, y, n-1)
def fung(x, y, n):
    return x + y*n

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if sm(i,j,k) == fung(i,j,k):
                print("True")
            else:
                
                print("False")
