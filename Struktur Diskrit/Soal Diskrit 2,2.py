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
valid = False
print("Rumus : ")
print("(p & q) -> p")
for q in range(0,2):
    for p in range(0,2):
        if check(implies(p and q,p)) == 1:
            valid = True
            break
if valid == True:
    print("Valid\n")
else:
    print("INVALID!\n")
valid = False
print("Rumus : ")
print("p -> (p v q)")
for q in range(0,2):
    for p in range(0,2):
        if check(implies(p,(p or q))) == 1:
            valid = True
            break
if valid == True:
    print("Valid\n")
else:
    print("INVALID!\n")
valid = False
print("Rumus : ")
print("[(p v q) & !p] -> q")
for q in range(0,2):
    for p in range(0,2):
        if check(implies((p or q)and nt(q),q)) == 1:
            valid = True
            break
if valid == True:
    print("Valid\n")
else:
    print("INVALID!\n")
valid = False

print("Rumus : ")
print("[(p -> q) & (r -> s) & (p v r)] -> (q v s)")
for q in range(0,2):
    for p in range(0,2):
        for r in range(0,2):
            for s in range(0,2):
                if check(implies((implies(p,q))and(implies(r,s))and(p or r),(q or s))) == 1:
                    valid = True
                    break
if valid == True:
    print("Valid\n")
else:
    print("INVALID!\n")
valid = False

print("Rumus : ")
print("[(p -> q) & (r -> s) & (!q v !s)] -> (!p v !r)")
for q in range(0,2):
    for p in range(0,2):
        for r in range(0,2):
            for s in range(0,2):
                if check(implies((implies(p,q))and(implies(r,s))and(nt(q) or nt(s)),(nt(q) or nt(s)))) == 1:
                    valid = True
                    break
if valid == True:
    print("Valid")
else:
    print("INVALID!\n")
