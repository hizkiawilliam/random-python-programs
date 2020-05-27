"""
    PROGRAM ENCRYPTER DECRYPTER v3.3
    by : Hizkia William Eben

    Program dibuat menggunakan Python v3.6.6
    Merupakan modifikasi Tugas LAB Dasar-dasar Pemrograman Modul 4

    Tujuan penggunaan untuk mengenkripsi dan dekripsi code
    Menggunakan prinsip Caesar Cypher yang dikembangkan

    Change log:
    v1.0 - Program akhir LAB DDP1 Modul 4
    v2.0 - Program dapat berjalan terus
         - Opsi Enkripsi atau Dekripsi
    v3.0 - Function Enkripsi dan Dekripsi
         - Comment untuk setiap line
         - Mendukung enkripsi/dekripsi kalimat
    v3.2 - User friendly
         - Change log
         - Help menu
         - Cara kerja
    v3.3 - Menggabung fungsi encrypt dan decrypt jadi satu
    Cara Kerja : (lihat bawah program)
"""
print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")  
print("<<< Program Enkripsi Dekripsi >>>")  #judul
print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>\n")  

#define fungsi untuk enkripsi
def encrypt(pesan,choice):
    hasil = ""      #buat variabel hasil berupa string kosong
    reverse2 = ""   #reverse2 string kosong untuk diisi string hasil reverse1
    count = 0       #counter sebagai check point pesan yang direverse
    for i in range(len(pesan)):             #loop setiap isi pesan
        split = pesan[count:count+key1:]    #memotong string menjadi bagian2 sesuai key 1
        reverse1 = split[::-1]              #membalik bagian yang telah dipotong
        count+=key1                         #memastikan loop dimulai dari huruf key+1
        reverse2 = reverse2 + reverse1      #memasukan potongan tadi kedalam string kosong reverse 2 
    for i in range(len(reverse2)):              #loop untuk melakukan Caesar Cypher
        if 97 <= ord(reverse2[i]) <= 122:       #memastikan pesan hanya berupa alfabet
            if choice == 1:
                code = ord(reverse2[i])%97 + key2   #menggeser ascii code setiap huruf sebanyak +key 2(encrypt)
            elif choice == 2:
                code = ord(reverse2[i])%97 - key2   #menggeser ascii code setiap huruf sebanyak -key 2(decrypt)
            hasil += chr((code%26) + 97)        #memasukan huruf kedalam hasil, memastikan ord tetap dialfabet setelah digeser
            success = True                      #membuat variabel bantuan
        else:
            print("Tidak bisa mengenkripsi non-alphabet \n")    #error handling jika memasukkan selain alfabet
            success = False
            break
    if success == True:
        return hasil                                #return hasil akhir
        
while(1):                                           #looping memulai program
    try:
        print("     Menu      ")
        print("===============")
        print("|1. Enkripsi  |")
        print("|2. Dekripsi  |")
        print("|3. Bantuan   |")
        print("===============")
        choice = int(input("Masukkan pilihan : "))  #input pilihan
        if choice == 1 or choice == 2:              #memastikan input hanya '1' atau '2'
            #meminta input
            key1 = int(input("Masukkan Key 1\t : ").lower())   #input key 1
            key2 = int(input("Masukkan Key 2\t : ").lower())   #input key 2
            pesan = input("Masukkan Pesan\t : ").lower()      #input pesan(dapat berupa kalimat)
            pesan_split = pesan.split()                     #memecah kalimat menjadi kata-kata
            final = ""                                      #string kosong untuk output
            if key1 == 0:
                key1 += key2
            for i in pesan_split:                       #loop untuk setiap kata pada kalimat
                final += encrypt(i,choice)                     #kata tersebut diproses fungsi encrypt
                final += " "                            #menambah spasi agar output menjadi kalimat
            print("Hasil enkripsi\t :",final,"\n")       #print output akhir
        elif choice == 3:
            print("-Pilih 1 untuk melakukan enkripsi, 2 untuk dekripsi")
            print("-Masukkan key 1")
            print("-Masukkan key 2")
            print("-Masukkan pesan yang akan dienkripsi/dekripsi\n")
                
        else:                                               #error handling jika pilihan diluar '1' atau '2'
            print("Pilihan tidak sesuai!\n")
    except:
        print("Pilihan tidak sesuai!\n")                    #error handling jika pilihan diluar angka
"""

    <<< Cara Kerja >>>
        
1. Input yang berupa kalimat dipecah menjadi kata
2. Setiap kata tersebut diproses masing-masing dalam fungsi Encrypt/Decrypt
3. Di dalam fungsi tersebut, terjadi beberapa proses:
    1. Melakukan proses pemenggalan dan pembalikan kata
        Memenggal pesan sesuai key 1
         Pesan masuk = bertanggungjawab
         Kunci = 3
         Pesan terpenggal = ber tan ggu ngj awa b
    
        Setelah itu tiap segment dibalik.
         Pesan dibalik = reb nat ugg jgn awa b
    
        Terakhir, setelah tiap segment dibalik, pesan kembali disatukan
         Hasil akhir = rebnatuggjgnawab
         
    2. Melakukan proses enkripsi Caesar Cypher
        Menggeser setiap ord kata berdasarkan key 2
         Kunci = 3
         Input proses = rebnatuggjgnawab
         Output proses = uheqdwxjjmjqdzd
4. Memasukkan setiap kata yang telah diproses ke dalam variabel final
5. Mencetak output dari final
    
"""
