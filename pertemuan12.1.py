
# Set
nomor = [1,1,2,3,5,5,7,8,9,0,4,4,6,8,8,9]
print (len(nomor))

# Mengubah menjadi set
# Set akan otomatis menghapus bilangan atau item yang sama
baru = set(nomor)
print (baru) # Hasilnya nanti {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print (len(baru))

# Masalah: Masukkan dalam data unik dalam posisi tidak ada yang sama
# Cara 1: Perulangan biasa
print ('CARA 1 PERULANGAN')
hasil = []
for nilai in nomor:
    if nilai not in hasil:
        hasil.append(nilai)
print (hasil) # Hasilnya nanti [1, 2, 3, 5, 7, 8, 9, 0, 4, 6]

# dir(list) untuk mengecek fungsi fungsi yang dapat digunakan dalam list
# dir(set) untuk mengecek fungsi fungsi yang dapat digunakan dalam set

# Cara 2: Menggunakan set
print ('CARA 2 SET')
hasil = set()
for nilai in nomor:
    hasil.add(nilai)
print (hasil) # Hasilnya {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print (list(hasil)) # Agar output dalam bentuk list
# Set tidak memperhitungkan urutan, otomatis menghaspus data yang sama
# Set tidak dapat diambil menggunakan indeks jadi menggunakan perulangan 

# .pop() mengambil dan menghapus salah satu data secara random
print ('POP')
a = {1,2,3,4}
print (a)
print(a.pop())
print (a)

# Menggunakan (discard) untuk menghapus suatu data yang diinginkan. *tanpa error jika data yang diinginkan dihapus tidak ada
print ('DISCARD')
a = {1,2,3,4}
print (a)
a.discard(3)
print (a)

# Menggunakan (remove) untuk menghapus suatu data yang diinginkan. *ada error jika data yang diinginkan dihapus tidak ada
print ('REMOVE')
a = {1,2,3,4}
print (a)
a.remove(4)
print (a)

# Menggunakan (clear) untuk menghapus seluruh data yang ada
print ('CLEAR')
a = {1,2,3,4}
print (a)
a.clear()
print (a)

# Untuk mengganti data dalam set harus dihapus dulu baru ditambahkan tidak bisa langsung menggunakan fungsi replace

