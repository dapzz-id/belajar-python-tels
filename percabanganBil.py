bil1 = input("Masukkan bilangan pertama: ")
bil2 = input("Masukkan bilangan kedua: ")

if(bil1 > bil2):
    hasil = 'Lebih besar!'
elif(bil1 < bil2):
    hasil = 'Lebih kecil!'
else:
    hasil = 'Sama dengan nilainya'

print('Bilangan', bil1, hasil, 'daripada bilangan ', bil2)