result = 0
num = [1,2,3,4,5,6]
for i in range(0,6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            result = result + num[i]+num[j]+num[k]
            if i!=j and j!=k and result%2==0:
                result = 0
                print(num[i],num[j],num[k]) 
    
