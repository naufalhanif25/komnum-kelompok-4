def input_pengguna():
  x0 = float(input("Masukkan nilai pendekatan awal (x0): "))
  e = float(input("Masukkan nilai toleransi error (e) : "))   
  N = int(input("Masukkan nilai iterasi maksimum (N): "))
    
  N = min(N, 10)
    
  return x0, e, N
