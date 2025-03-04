listKota = [
    'Jakarta',
    'Surabaya',
    'Depok',
    'Bekasi',
    'Solo',
    'Yogyakarta',
    'Semarang',
    'Makassar'
]

kotaYangDicari = input('Ketik nama kota yang ingin dicari: ')

for i, kota in enumerate(listKota):
    if kota.lower() == kotaYangDicari.lower():
        print('Kota yang Anda cari berada pada indeks', i)
        break
else:
    print('Kota yang Anda cari tidak ditemukan')