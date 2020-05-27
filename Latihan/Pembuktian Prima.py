
def prime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number\n")
               break
       else:
           print(num,"is a prime number\n")
    else:
       print(num,"is not a prime number\n")


for i in range (1,100):
    y = i**2 + i + 41
    print("Untuk i : ",i)
    prime(y)
