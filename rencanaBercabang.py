print("Rencana setelah lulus sekolah?\n1. Kuliah\n2. Kerja")
jawaban = input("Masukkan pilihan: ")

if(jawaban == "1"):
    print("\nKuliah jurusan apa? \n1. Teknik Industri \n2. Kedokteran")
    jawab = input("Masukkan pilihan: ")
    if(jawab == "1"):
        print("\nKuliah di Teknik Industri")
    else:
        print("\nKuliah di Kedokteran")
else:
    print("\nKerja di Industri apa? \n1. Tambang \n2. Teknologi")
    jawab = input("Masukkan pilihan: ")
    if(jawab == "1"):
        print("\nKerja di Industri Pertambangan")
    else:
        print("\nKerja di Industri Teknologi")