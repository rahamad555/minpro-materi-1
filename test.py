# prongam menghitung harga barang berdasarkan harga barang dan jumalah pembelian 

#login sederhana user dan NIM
print("login menggunakan nama,NIM,\n")
nama = input("masukan nama: ") # input nama

# Proses input NIM dengan menggunakan while untuk terus meminta input NIM hingga pengguna memasukkan NIM yang benar (berupa angka).
while True: 
    nim = input("Masukkan NIM: ")
    if nim.isdigit(): # Mengecek apakah NIM hanya berisi angka
        break # Jika benar, loop akan berhenti dengan break
    else: # Jika salah(ada huruf atau selain angka), program akan meminta user untuk input nim ulang dan akan diberi peringatan
        print("Tolong isi dengan angka dan bukan huruf!")

# menampilkan Selamat datang atau sapaan untuk user
print("\nSelamat datang", nama,  "dengan NIM", nim,)

while True: # menggunakan while untuk mengulang pertanyaan atau menhitung total harga barang dan total pembelian 
    # gunakan input untuk total harga barang berdasrkan harga barang dan total pembelian 
    harga_barang  = float(input("Masukan harga barang: "))
    jumlah_barang = int(input("Masukan jumlah pembelian: "))  
    total_harga = harga_barang * jumlah_barang # rumus atau perhitungan untuk mencari total harga

    # membuat percabangan untuk mentukan apakah total harga lebih dari Rp 250000
    # jika lebih tambahkan diskosn sebesar 25% dari total harga 
    # jika tidak melebihi atau tidak mencapai Rp 250000, maka tidak mendapatkan diskon 
    # Cek jika total harga lebih dari Rp. 250,000
    if total_harga > 250000:
        # Hitung diskon
        diskon = total_harga * 0.25
        total_harga -= diskon
        print("\nSelamat anda mendapatkan diskon sebesar 25% dari total_harga")
        print(" ini adalah total harga anda setelah mendapat diskon: ", total_harga) # menampilkan total harga yang sudah di potong dengan diskon

    else:
        print("\nMaaf anda tidak mendapat diskon  karena total harga anda tidak melebihi 250000")
        print("ini adalah total harga anda sekrang:", total_harga) #menampilkan harga yang tidak mendapat diskon 

    # menerapkan perulangan untuk memberikakn pilihan apakah ingin menghitung harga atau keluar 
    print('\nSilahkan pilih pilihan berikut:\n 1.ingin menghitung total harga lagi?\n 2.keluar dari program\n') # pilihan untuk user apakah user mau menghitung total harga lagi atau tidak
    pilihan = int(input('Masukkan pilihan anda(nomor 1 atau 2): ')) 
    if pilihan == 1: 
        continue #user akan menghitung harga lagi jika memilih nomor 1
    elif pilihan == 2:
        print("\nTerima Kasih telah menggunakan program  ini. anda akan dikeluarkan dari program ini dan selamat tinggal!")

    else:
        print("\nMaaf, Pilihan tidak ada. Anda akan secara otomatis dikeluarkan dalam program ini")
        
