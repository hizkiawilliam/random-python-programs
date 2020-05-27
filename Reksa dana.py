num = int(input("Input initial money : "))
initial = num
interest = float(input("Input interest : "))
year = int(input("Input year : "))

for i in range(0,year):
    for i in range(0,12-1):
        initial += num
        #print(initial)
    initial += initial * interest/100
    #print("Next year ",initial)

print("Final : Rp.",initial)
