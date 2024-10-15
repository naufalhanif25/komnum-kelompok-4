import tkinter as tk
from tkinter import ttk

# Membuat window utama
root = tk.Tk()
root.title("Contoh Tabel dengan Border pada Setiap Kolom di Tkinter")

# Mengatur style untuk Treeview
style = ttk.Style()
style.configure("Treeview", rowheight=30)
style.configure("Treeview.Heading", background="lightgrey", font=("Arial", 10, "bold"))
style.map("Treeview.Heading", background=[('active', 'lightblue')])

# Membuat Treeview (tabel)
tabel = ttk.Treeview(root, columns=("ID", "Nama", "Umur"), show="headings")
tabel.pack(padx=10, pady=10)

# Menentukan kolom-kolom pada tabel
tabel.column("ID", anchor=tk.CENTER, width=100)
tabel.column("Nama", anchor=tk.W, width=150)
tabel.column("Umur", anchor=tk.CENTER, width=100)

# Menambahkan heading (judul kolom)
tabel.heading("ID", text="ID", anchor=tk.CENTER)
tabel.heading("Nama", text="Nama", anchor=tk.W)
tabel.heading("Umur", text="Umur", anchor=tk.CENTER)

# Menambahkan data ke dalam tabel
data = [
    ("1", "Alice", "25"),
    ("2", "Bob", "30"),
    ("3", "Charlie", "22"),
    ("4", "David", "28"),
]

for row in data:
    tabel.insert(parent='', index='end', iid=row[0], text='', values=row)

# Menambahkan scrollbar untuk tabel
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tabel.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Menghubungkan scrollbar dengan tabel
tabel.configure(yscrollcommand=scrollbar.set)

# Menjalankan aplikasi
root.mainloop()
