pwd_benar = 'si23d'
a = True
limit = 3
i = 0

while a:
    i += 1
    pwd = input('masukkan password')
    if pwd == pwd_benar:
        print('password benar! selamat anda login')
        a = False
    else:
        print('password salah!')
        if i == limit:
            print('kesempatan anda habis')
            a = False
        else:
            print(f'kesempatan anda tersisa {limit-i} kali')




# tugas: buat password berlapis 3 
# jika salah: passwod salah, anda gagal pada halaman 1
# jika salah: passwod salah, anda gagal pada halaman 2       
# jika salah: passwod salah, anda gagal pada halaman 3
# jika benar: passwod salah, selamat datang di pada halaman 1       
























