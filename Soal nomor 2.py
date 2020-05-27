tests = int(input())
length = []
content = {}
def check(lst):
    sort = True
    for i in range(0,len(lst)-1):
        if lst[i] <= lst[i+1]:
            sort = True
        else:
            sort = False
    return lst.sort()


def sorting(lst):
    temp = list(lst)
    count = 0
    for i in range(0,len(lst)):
        print(lst[count:count+3])
        count += 3

if 1<=tests<=10:
    for i in range(0,tests):
        length.append(int(input()))
        if 3<=length[i]<=1000:
            content[length[i]] = input()
        else:
            print("Out of constrains!")
else:
    print("Out of constrains!")
for k in content:
    if k == len(content[k]):
        print(sorting(content[k]))
    else:
        print("Out of constrains!")

        


    



    
