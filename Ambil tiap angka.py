def sat(var):
    return int(var%10)

def pul(var):
    return int(((var-(var%10))/10)%10)

def rat(var):
    return int(((var-(var%100))/100)%100%10)

def rib(var):
    return int(((var-(var%1000))/1000)%1000%100%10)

def pulrib(var):
    return int(((var-(var%10000))/10000)%10000%1000%100%10)

num = int(12345)
print(sat(num))
print(pul(num))
print(rat(num))
print(rib(num))
print(pulrib(num))
