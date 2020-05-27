modal = 10000000
percent = 2
days = 22
month = 12
total = 0

for i in range(1,month+1):
    for j in range(1,days+1):
        profit = percent/100*modal
        modal = modal + profit
        #print("Day\t\t: ",i)
        #print("Profit\t\t: ",round(profit))
        #print("Money\t\t: ",round(modal),"\n")
    monthprofit = modal
    total = modal + profit
    print("Month\t\t: ",i)
    print("Profit\t\t: ",round(monthprofit))
    print("Money\t\t: ",round(total),"\n")
