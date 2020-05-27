num = int(input())
cases = []
for i in range(0,num):
    cases.append(int(input()))

for x in cases:
    n1 = 1
    n2 = 2
    count = 1
    if x <= 0:
        pass
    elif x == 1:
        print(n1)
    else:
        while count < x:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
        print(n1%10)
        


    
    
