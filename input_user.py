#Fungsi untuk meminta input dari pengguna
def input_pengguna():
  
  #Meminta pengguna untuk memasukkan nilai pendekatan awal, toleransi error, dan iterasi maks
  x0 = float(input("Masukkan nilai pendekatan awal (x0): "))
  e = float(input("Masukkan nilai toleransi error (e) : "))   
  N = int(input("Masukkan nilai iterasi maksimum (N): "))

  #Membatasi jumlah iterasi maksimum menjadi 10
  N = min(N, 10)

  #Mengembalikan nilai x0, e, dan N 
  return x0, e, N
