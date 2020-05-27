'''def penjumlahandiri(var):
    var = [int (a) for a in str(var)]
    return sum(var)

while(True):
    inp = int(input())
    pecah = [int (i) for i in str(inp)]
    sum(pecah)
    if sum(pecah) < 10:
        print(sum(pecah))
    else:
        print(penjumlahandiri(sum(pecah)))
    '''


def func(num):
    print(num) if int(num) < 10 else func(int(sum(int (i) for i in [int (i) for i in str(num)])))
        
while(True):
    func(str(input()))


