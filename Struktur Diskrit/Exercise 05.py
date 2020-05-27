num = int(input("Masukkan angka: "))
lst = ""
for i in range(1, num + 1):
    if num % i == 0 and i != num:
        lst += str(i)
        lst += ", "
    elif num % i == 0:
        lst += str(i)
print("Hasil faktor dari",num,"adalah "+lst)
        
