# Membuat dictionary untuk menyimpan menu dan harga
menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Goreng": 18000,
    "Sate Ayam": 20000,
    "Soto Ayam": 15000
}

# Menampilkan menu kepada pengguna
print("Selamat datang di Nasgor Tambun!")
print("Berikut adalah menu yang tersedia:")
for item, price in menu.items():
    print(f"{item}: Rp {price}")

# Meminta pengguna memasukkan pesanan
pesanan = input("Masukkan pesanan Anda (Jika lebih pisahkan dengan koma): ")

# Memisahkan pesanan menjadi daftar makanan
daftar_pesanan = pesanan.split(",")

# Menghitung total harga pesanan
total_harga = 0
for item in daftar_pesanan:
    item = item.strip()  # Menghapus spasi di awal dan akhir item
    if item in menu:
        total_harga += menu[item]
    else:
        print(f"Maaf, {item} tidak ada dalam menu.")

# Menampilkan total harga pesanan
print(f"Total harga pesanan Anda adalah: Rp {total_harga}")