num_input = int(input("Input integer : "))
num = num_input
rem = []
while num != 0:
    rem.append(num % 8)
    num = num//8
rem = rem[::-1]
print(num_input,"dec to oct is ",end="")
for i in range(0,len(rem)):
    print(rem[i],end="")
print("\n")
    
    


