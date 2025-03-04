bilangan = int(input('Masukkan Bilangan: '))
hasil = int(input('Masukkan Hasil Pangkat: '))

# Mencari pangkat dengan mencoba nilai dari 0 hingga hasil
pangkat = 0
while pow(bilangan, pangkat) < hasil:
    pangkat += 1

# Memeriksa apakah hasil yang ditemukan benar
if pow(bilangan, pangkat) == hasil:
    print(f'Bilangan {bilangan} dipangkatkan {pangkat} menghasilkan {hasil}')
else:
    print(f'Tidak ditemukan pangkat yang menghasilkan {hasil} dari bilangan {bilangan}')