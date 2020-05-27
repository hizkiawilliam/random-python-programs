def implies(a,b):
    if b == 0 or a == 0:
        return 0
    elif a == 1 and b == 1:
        return 1
def nt(a):
    if a == 0:
        return 1
    elif a == 1:
        return 0
def check(a):
    if a == 1:
        return True
    elif a == 0:
        return False
print("Rumus : ")
print("(q -> [(!p v r) & !s]) & [!s -> (!r & q)]")
for q in range(1,2):
    for p in range(0,2):
        for r in range(0,2):
            for s in range(0,2):
                print(" q = ",check(q),end="")
                print(" p = ",check(p),end="")
                print(" r = ",check(r),end="")
                print(" s = ",check(s),end="")
                print(" Result = ",check((implies(q,(nt(p) or r)and nt(s))) and (implies(nt(s),(nt(r)and q)))))
