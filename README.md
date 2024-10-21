UTS LAB KOMPUTASI NUMERIK

Penyelesaian Persamaan Non linier dengan Metode Iterasi yang diimplementasikan menggunakan code Pyhton.

ANGGOTA KELOMPOK 4 :
- ADINDA MUARRIVA (2308107010001)
- NAUFAL HANIF (2308107010025)
- NADIA MAGHDALENA (2308107010045)
- NURUL IZZATI (2308107010047)
- RAHMAD HIDAYATULLAH TSUNAMI (2308107010051)
- MUHAMMAD RAYYANTA ADHABARUS (2308107010053)

Metode iterasi adalah teknik numerik yang digunakan untuk menemukan solusi dari persamaan matematis, biasanya dalam bentuk persamaan non-linear. Prinsip dasar metode ini adalah memulai dengan sebuah tebakan awal untuk solusi dan kemudian mengiterasi atau memperbarui tebakan tersebut melalui rumus tertentu hingga mencapai tingkat ketelitian yang diinginkan.Metode iterasi sering digunakan dalam berbagai aplikasi, seperti optimasi, analisis numerik, dan pemecahan sistem persamaan. Keberhasilan metode ini sangat bergantung pada pilihan tebakan awal dan sifat fungsi yang dianalisis.

File main.py : File ini merupakan aplikasi berbasis GUI menggunakan pustaka tkinter. Aplikasi menerima input dari pengguna, seperti fungsi matematis (fx dan gx), nilai awal, jumlah iterasi, dan batas kesalahan. Setelah input diterima, aplikasi menjalankan perhitungan iteratif menggunakan fungsi dari modul iteration_algorithm.py, dan menampilkan hasilnya dalam tabel. Aplikasi ini juga memiliki opsi untuk menampilkan hasil perhitungan dalam bentuk grafik dengan bantuan modul plots.py.

File iteration_algorithm.py: File ini berisi fungsi utama untuk melakukan perhitungan iteratif. Fungsi iteration_algorithm menggunakan dua fungsi input dari pengguna (fx dan gx), serta nilai awal, jumlah iterasi, dan batas kesalahan untuk menghitung hasil iterasi. Hasil perhitungan ini disimpan dalam bentuk daftar yang mencakup nilai-nilai x, g(x), dan f(x) dari setiap iterasi, dan dikembalikan untuk ditampilkan di antarmuka yang dibuat dalam main.py.

