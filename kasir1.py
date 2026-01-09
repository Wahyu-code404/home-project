#program kasir sederhana menggunakan struktur pemilihan

#{I.S.: pengguna memilih menu dan memasukan tanggal, jam, nama pemesan dan memasukan menu makanan, minuman,
#       jumlah item dan potongan harga (jika ada)}
#{F.S.: menampilkan struk pesanan dengan nama item dan harga di dalam nya}

import os

#pilihan menu
os.system('cls')
print('         SELAMAT DATANG DITOKO IMPIAN ANDA         ')
print('')
print('===================================================')
print('|            MENU             |    DAFTAR HARGA   |')
print('===================================================')
print('| M1. AYAM + TAHU TEMPE       |      RP.15000     |')
print('| M2. NASI AYAM PENYET KOMPLIT|      RP.16000     |')
print('| M3. NASI KUNING EROPA       |      RP.10000     |')
print('| M4. INDOMI BAKAR KOMPLIT    |      RP.8000      |')
print('| M5. NASI GORENG BUDIONO     |      RP.15000     |')
print('===================================================')

#PENGGUNA MEMASUKAN MENU MAKANAN
print('--->MASUKAN PILIHAN MENU ANDA DISINI<---')
Tanggal = (input('masukan tanggal      :')).upper() 
Jam = (input('Masukan jam          :'))
Atasnama = (input('Masukan nama pemesan :')). upper()
Nomenu = (input('No Menu              :')). upper()
Jumlahmenu= int(input('Jumlah Menu          :'))
os.system('pause')
os.system('cls')

#pilihan minuman
print('SELAMAT DATANG DITOKO IMPIAN ANDA')
print('')
print('=============================')
print('|   MINUMAN    |   HARGA    |')
print('=============================')
print('| 1. ES TEH     |   RP.3000 |')
print('| 2. TEH ANGET  |   RP.2000 |')
print('| 3. ES JERUK   |   RP.4000 |')
print('| 4. TEH BOTOL  |   RP.5000 |')
print('| 5. ES KELAPA  |   RP.5000 |')
print('=============================')

#PENGGUNA MEMASUKAN MENU MINUMAN 
print('--->MASUKAN PILIHAN MINUMAN ANDA DISINI<---')
Nominuman = (input('No Minuman :'))
Jumlahminuman = int(input('Jumlah     :'))
os.system('pause')
os.system('cls')

#validasi kode menu
if (Nomenu not in ['M1', 'M2', 'M3', 'M4','M5']):
    print('-->PILIHAN MENU TIDAK TERSEDIA<--!')
    exit()


#validasi nomer menu, nama menu, dan harga satuan
if Nomenu == "M1":
    NamaMenu = "NASI AYAM + TAHU TEMPE"
    HargaSatuan = 15000
elif Nomenu == "M2":
    NamaMenu = "NASI AYAM PENYET KOMPLIT"
    HargaSatuan = 16000
elif Nomenu == "M3":
    NamaMenu= "NASI KUNING EROPA"
    HargaSatuan = 10000
elif Nomenu == "M4":
    NamaMenu= "INDOMI BAKAR KOMPLIT"
    HargaSatuan = 8000
elif Nomenu == "M5":
    NamaMenu= "NASI GORENG BUDIONO"
    HargaSatuan = 15000

#validasi kode minuman
if (Nominuman not in ['1', '2', '3', '4','5']):
    print('-->PILIHAN Minuman TIDAK TERSEDIA<--!')
    exit()

#validasi nomer minuman, nama minuman, harga satuan
if Nominuman == "1":
    NamaMimuman = "ES TEH"
    Harga = 3000
elif Nominuman == "2":
    NamaMimuman = "TEH ANGET"
    Harga = 2000
elif Nominuman == "3":
    NamaMimuman= "ES JERUK"
    Harga = 5000
elif Nominuman == "4":
    NamaMimuman= "TEH BOTOL"
    Harga = 5000
elif Nominuman == "5":
    NamaMimuman= "ES KELAPA"
    Harga = 5000

#HITUNG PESANAN
TotalMenu = Jumlahmenu * HargaSatuan
TotalMinuman = Jumlahminuman * Harga
TotalPesanan = TotalMenu + TotalMinuman

#tampil hasil sebelum bayar
print(f'NAMA MENU    : {NamaMenu}')
print(f'HARGA        : {HargaSatuan}')
print(f'Jumlah       : {Jumlahmenu}')
print(f'Total        : {TotalMenu}')
print()
print(f'NAMA MINUMAN : {NamaMimuman}')
print(f'HARGA        : {Harga}')
print(f'Jumlah       : {Jumlahminuman}')
print(f'Total        : {TotalMinuman}')
print()
print(f'Total        : {TotalPesanan}')

os.system('pause')
uang = int(input('NominaL       :'))
Diskon = str(input('Masukan potongan harga (jika ada) :'))

#validasi kode diskon
if (Diskon not in ['0','10', '20', '25']):
    print('-->DISKON TIDAK TERSEDIA<--!')
    exit()

#validasi diskon
if Diskon =="0":
    Jdiskon = 0
elif Diskon == "10":
    Jdiskon = 0.1
elif Diskon == "20":
    Jdiskon = 0.2
elif Diskon == "25":
    Jdiskon = 0.25

#menghitung potongan harga 
Potongan = int (Jdiskon * TotalPesanan)
Tdiskon = int (TotalPesanan - Potongan)
Kembalian = uang - Tdiskon

os.system('pause')
os.system('cls')
#tampil hasil sesudah bayar
print('===========STRUK BELANJAAN==========')
print(f'Tanggal          : {Tanggal}')
print(f'Jam              : {Jam}')
print(f'Atas nama        : {Atasnama}')
print()
print('====================================')
print(f'NAMA MENU        : {NamaMenu}')
print(f'HARGA            : {HargaSatuan}')
print(f'Jumlah           : {Jumlahmenu}')
print(f'Total menu       : {TotalMenu}')
print('=====================================')
print(f'NAMA MINUMAN     : {NamaMimuman}')
print(f'HARGA            : {Harga}')
print(f'Jumlah           : {Jumlahminuman}')
print(f'Total menu       : {TotalMinuman}')
print('=====================================')
print(f'Total Pesanan    : {TotalPesanan}')
print(f'Potongan         : {Potongan}')
print('=====================================')
print(f'Total pesanan    : {Tdiskon}')
print(f'Uang pembayaran  : {uang}')
print(f'Kembalian        : {Kembalian}')
print('=============terima kasih============')
print('=============good byeeeee============')
os.system('pause')
os.system('cls')





