def negative(lst):
    neg = False
    for i in range(0,len(lst)):
        if lst[i]<0:
            return i
            neg = True
            break
    if neg == False:
        return -1
