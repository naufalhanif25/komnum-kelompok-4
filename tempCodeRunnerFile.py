tabel['columns'] = ('ID', 'Nama', 'Umur')

# Membuat heading (judul kolom)
tabel.column("#0", width=0, stretch=tk.NO)  # kolom tak terlihat (default kolom)
tabel.column("ID", anchor=tk.CENTER, width=80)
tabel.column("Nama", anchor=tk.W, width=150)
tabel.column("Umur", anchor=tk.CENTER, width=80)

# Menambahkan teks heading pada kolom-kolom
tabel.heading("#0", text="", anchor=tk.CENTER)
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