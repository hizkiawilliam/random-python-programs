r1 = int(20)
r2 = int(20)
r3 = int(20)
empty1 = False
empty2 = False
empty3 = False
print("Isi kotak 1 : ",r1)
print("Isi kotak 2 : ",r2)
print("Isi kotak 3 : ",r3)
r = input("Pilih kotak 1, 2 atau 3 : ")
if r == 1:
    k1 = input("Ambil jumlah kelereng : ")
    r1 = r1 - k1
if r == 2:
    if r2 == 0:
        empty2 = True
    k2 = input("Ambil jumlah kelereng : ")
    r2 = r2 - k2
if r == 2:
    if r3 == 0:
        empty3 = True
    k3 = input("Ambil jumlah kelereng : ")
    r3 = r3 - k3
    
