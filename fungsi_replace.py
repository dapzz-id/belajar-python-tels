teks = input('Ketik sesuatu: ')
pengganti = input('Masukkan huruf yang ingin diganti: ')
huruf = input('Huruf apa yang akan diganti: ')

# teks = teks.replace('a', pengganti)
# teks = teks.replace('i', pengganti)
# teks = teks.replace('u', pengganti)
# teks = teks.replace('e', pengganti)
# teks = teks.replace('o', pengganti)

teks = teks.replace(pengganti.capitalize(), huruf)
teks2 = teks.replace(pengganti.lower(), huruf)

print(teks2)