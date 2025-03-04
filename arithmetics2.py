import datetime

def hitung_umur(tanggal_lahir):
    tanggal_sekarang = datetime.date.today()
    tahun_lahir, bulan_lahir = tanggal_lahir.split('-')
    tahun_sekarang = tanggal_sekarang.year
    bulan_sekarang = tanggal_sekarang.month

    umur_tahun = tahun_sekarang - int(tahun_lahir)
    umur_bulan = bulan_sekarang - int(bulan_lahir)

    if umur_bulan < 0:
        umur_tahun -= 1
        umur_bulan += 12

    return umur_tahun, umur_bulan

tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM): ")
umur_tahun, umur_bulan = hitung_umur(tanggal_lahir)
print("Umur Anda adalah {} tahun {} bulan.".format(umur_tahun, umur_bulan))