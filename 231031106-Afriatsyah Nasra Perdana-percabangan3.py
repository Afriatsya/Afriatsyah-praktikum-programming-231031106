nama = input("Masukkan nama karyawan: ")
pendapatan = input("Masukkan besaran pendapatan: ")
pendapatan = int(pendapatan)

print("Nama karyawan:", nama)

print("Pendapatan karyawan:", pendapatan)

if pendapatan > 1000:
    print("Status: Berhak")
else:
    print("Status: Tidak Berhak")