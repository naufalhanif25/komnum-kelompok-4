from fungsi import F, G
from tabel import tampilkan_hasil_iterasi

def iterasi_sederhana(x0, e, N):
    #Melakukan iterasi sederhana untuk menemukan akar dari persamaan
    iterasi = 0
    x = x0
    hasil_iterasi = []

    #Proses iterasi
    while abs(F(x)) >= e and iterasi < N:
        #Simpan hasil setiap iterasi
        hasil_iterasi.append([iterasi + 1, x, G(x), F(x)])
        
        #Update nilai untuk iterasi berikutnya
        iterasi += 1
        x = G(x)

    #Tampilkan hasil iterasi dalam tabel
    tampilkan_hasil_iterasi(hasil_iterasi)

    #Tentukan iterasi terakhir yang akan diambil
    iterasi_terakhir = min(10, len(hasil_iterasi))
    x_terakhir = hasil_iterasi[iterasi_terakhir - 1][1]

    #Tampilkan hasil akhir
    print(f"\nAkar ditemukan: x terakhir (iterasi ke-{iterasi_terakhir}) = {x_terakhir:.6f}")
