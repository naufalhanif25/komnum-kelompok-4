import tkinter as tk
from  tkinter import ttk
from numpy import *
import matplotlib
import string
import re
import os

#Fungsi untuk mengubah operator dan simbol matematika ke dalam sintaks python
def convert_function(input_func):
    #Mengganti simbol pangkat, perkalian, dan pembagian
    input_func = input_func.replace("^", "**").replace("\u00D7", "*").replace("\u00F7", "/")
    
    #Menambahkan simbol perkalian antara angka dan variabel x
    input_func = re.sub(r"(\d)(x)", r"\1*x", input_func)

    #Mengganti simbol pi dengan 'pi'
    input_func = input_func.replace("\u03C0", "pi")

    #Menambahkan tanda perkalian antara angka dengan 'pi'
    input_func = re.sub(r"(\d)(pi)", r"\1*pi", input_func)

    final_func = input_func.lstrip("*")
    return final_func

#Fungsi untuk memasukkan nilai x ke dalam fungsi dan mengevaluasi hasilnya
def insert_func_value(func_input, x):
    func = convert_function(func_input) #Mengonversi fungsi input ke dalam format yang dapat dievaluasi python

    try:
        result = eval(func, {"x": x, "pi": pi, "abs": abs, "exp": exp, "sqrt": sqrt, 
                            "sin": sin, "cos": cos, "tan": tan, 
                            "log": log, "log2": log2, "log10": log10})

        return result
    except Exception as e:
        print("Error:", e) #Print error jika evaluasi gagal

#Fungsi untuk menampilkan f(x)
def function():
    print("f(x)")

#Fungsi untuk menampilkan metode iterasi
def iteration_method():
    print("Metode iterasi")

#Fungsi untuk menampilkan tabel
def table():
    print("Tabel")

#Fungsi untuk menampilkan plot
def plot():
    print("Plot")

#Fungsi untuk menangani klik pada entri input
def on_entry_click(event):
    global clicked_entry
    #Menyimpan entri yang diklik sebagai entri aktif
    clicked_entry = event.widget

#Fungsi untuk mengubah warna 
def on_focus_in(event):
    event.widget.config(highlightcolor = HIGHLIGHT_COLOR) #Mengatur warna highlight saat entri aktif

#Fungsi untuk mengubah warna saat entri kehilangan fokus 
def on_focus_out(event):
    if event.widget.get() == "":
        #Mengatur entri ke warna dasar saat entri kosong
        event.widget.config(highlightcolor = BASE_COLOR)
    else:
        #Mengatur entri ke warna highlight saat entri terisi
        event.widget.config(highlightcolor = HIGHLIGHT_COLOR)

#Fungsi untuk memindahkan fokus dari label ke elemen lain
def focus_out_entries(label):
    label.focus_set()

#Fungsi untuk memindahkan fokus ke entri berikutnya
def focus_next_entry(event, next_entry):
    next_entry.focus_set()

#Fungsi untuk menyisipkan simbol ke dalam entri yang aktif
def insert_symbol(symbol):
    #Mendapatkan posisi kursor di entri yang aktif
    cursor_position = clicked_entry.index(tk.INSERT)
    #Menyisipkan simbol pada posisi kursor
    clicked_entry.insert(cursor_position, symbol)

#Fungsi untuk menghapus karakter terakhir dari entri aktif
def backspace():
    current_string = clicked_entry.get() #Mendapatkan teks dari entri

    if current_string:
        new_string = current_string[:-1] #Menghapus karakter terakhir

        clicked_entry.delete(0, tk.END) #Menghapus teks dari entri
        clicked_entry.insert(0, new_string) #Memasukkan kembali teks yang sudah diubah

#Fungsi untuk menyembunyikan label
def hide_label(label):
    label.config(text = "")

#Fungsi untuk memproses output berdasarkan input user
def output_processing():
    global func_fx , func_gx, first_x, N_iter, error

    focus_out_entries(output_label)

    try:
        func_fx = entry_fx.get() #Mendapatkan fungsi f(x)
        func_gx = entry_gx.get() #Mendapatkan fungsi g(x)

        first_x = entry_x1.get() #Mendapatkan nilai x awal
        first_x = float(first_x) #Mengonversi x jadi float

        N_iter = entry_N_iter.get() #Mendapatkan jumlah iterasi maksimum
        N_iter = int(N_iter) #Mengonversi jumlah iterasi menjadi integer

        error = entry_error.get() #Mendapatkan nilai toleransi error
        error = float(error) #Mengonversi nilai toleransi error menjadi float

        #Mengevaluasi fungsi f(x) dan g(x) dengan nilai awal x
        fx = insert_func_value(func_fx, first_x)
        gx = insert_func_value(func_gx, first_x)

        #Menampilkan notifikasi 'sukses'
        announce_label.config(text = "Success", fg = SUCCESS_COLOR)
        #Menghilangkan notifikasi setelah 3 detik
        interface.after(3000, hide_label, announce_label)

        #Menampilkan hasil evaluasi f(x)
        result_label.config(text = f"x = {fx}")
    except Exception as error_info:
        announce_label.config(text = "Error: " + str(error_info), fg = ERROR_COLOR) #Menampilkan pesan kesalahan jika error
        interface.after(3000, hide_label, announce_label)

        #Menampilkan hasil error
        result_label.config(text = f"x = NULL")


current_dir = os.path.dirname(__file__) #Mendapatkan direktori saat ini
data = [] #Menyimpan data hasil iterasi

#Definisi warna-warna untuk tampilan GUI
BACKGROUND_COLOR = "#FFFFFF"
FILL_COLOR = "#F1F2F6"
BUTTON_COLOR_1 = "#00A8FF"
BUTTON_COLOR_2 = "#FF4757"
BUTTON_COLOR_3 = "#ECCC68"
SUCCESS_COLOR = "#2ED573"
ERROR_COLOR = "#FF4757"
HIGHLIGHT_COLOR = "#00A8FF"
BASE_COLOR = "lightgray"
LASTROW_COLOR = "#7BED9F"

#Membuat main window untuk GUI
interface = tk.Tk()
interface.resizable(False, False) #Menonaktifkan opsi resize
interface.title("Metode Iterasi") #Memberikan judul
interface.iconbitmap(current_dir + "\\icon.ico") #Menampilkan ikon
interface.config(bg = BACKGROUND_COLOR) #Mengatur warna latar belakang

#Membuat label input
input_label = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Input", font = ("Arial", 12, "bold"), anchor = "center")
input_label.grid(padx = (20, 0), pady = (6, 0), row = 0, column = 0)

#Membuat label untuk fungsi f(x) dan g(x), nilai x awal, nilai iterasi N, dan nilai toleransi error
func_fx = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Fungsi f(x)", font = ("Arial", 8), anchor = "w")
func_fx.grid(padx = (20, 6), pady = (6, 0), row = 1, column = 0, sticky = "w")

func_gx = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Fungsi g(x)", font = ("Arial", 8), anchor = "w")
func_gx.grid(padx = (20, 6), pady = (6, 0), row = 2, column = 0, sticky = "w")

first_x = tk.Label(interface, bg = BACKGROUND_COLOR, text = "x awal", font = ("Arial", 8), anchor = "w")
first_x.grid(padx = (20, 6), pady = (6, 0), row = 3, column = 0, sticky = "w")

N_iteration = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Iterasi N", font = ("Arial", 8), anchor = "w")
N_iteration.grid(padx = (20, 6), pady = (6, 0), row = 4, column = 0, sticky = "w")

error = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Error", font = ("Arial", 8), anchor = "w")
error.grid(padx = (20, 6), pady = (6, 0), row = 5, column = 0, sticky = "w")

#Membuat entri untuk input pengguna
entry_fx = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_fx.config(highlightbackground = BASE_COLOR, highlightthickness = 1)
entry_fx.grid(padx = (12, 20), pady = (8, 0), row = 1, column = 1, sticky = "w")

entry_gx = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_gx.config(highlightbackground = BASE_COLOR, highlightthickness = 1)
entry_gx.grid(padx = (12, 20), pady = (8, 0), row = 2, column = 1, sticky = "w")

entry_x1 = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_x1.config(highlightbackground = BASE_COLOR, highlightthickness = 1)
entry_x1.grid(padx = (12, 20), pady = (8, 0), row = 3, column = 1, sticky = "w")

entry_N_iter = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_N_iter.config(highlightbackground = BASE_COLOR, highlightthickness = 1)
entry_N_iter.grid(padx = (12, 20), pady = (8, 0), row = 4, column = 1, sticky = "w")

entry_error = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_error.config(highlightbackground = BASE_COLOR, highlightthickness = 1)
entry_error.grid(padx = (12, 20), pady = (8, 0), row = 5, column = 1, sticky = "w")

entry_fx.bind("<Button-1>", on_entry_click)
entry_gx.bind("<Button-1>", on_entry_click)
entry_x1.bind("<Button-1>", on_entry_click)
entry_N_iter.bind("<Button-1>", on_entry_click)
entry_error.bind("<Button-1>", on_entry_click)

entry_fx.bind("<FocusIn>", on_focus_in)
entry_gx.bind("<FocusIn>", on_focus_in)
entry_x1.bind("<FocusIn>", on_focus_in)
entry_N_iter.bind("<FocusIn>", on_focus_in)
entry_error.bind("<FocusIn>", on_focus_in)

entry_fx.bind("<FocusOut>", on_focus_out)
entry_gx.bind("<FocusOut>", on_focus_out)
entry_x1.bind("<FocusOut>", on_focus_out)
entry_N_iter.bind("<FocusOut>", on_focus_out)
entry_error.bind("<FocusOut>", on_focus_out)

entry_fx.bind("<Return>", lambda event: focus_next_entry(event, entry_gx))
entry_gx.bind("<Return>", lambda event: focus_next_entry(event, entry_x1))
entry_x1.bind("<Return>", lambda event: focus_next_entry(event, entry_N_iter))
entry_N_iter.bind("<Return>", lambda event: focus_next_entry(event, entry_error))

#Menentukan posisi baris dan kolom pada tombol kalkulator
calc_buttons = [
    ("7", 1, 2), ("8", 1, 3), ("9", 1, 4), ("-", 1, 5), ("\u221A", 1, 6), ("\u03C0", 1, 7), ("x", 1, 8),
    ("4", 2, 2), ("5", 2, 3), ("6", 2, 4), ("\u00D7", 2, 5), ("(", 2, 6), ("sin", 2, 7), ("log", 2, 8),
    ("1", 3, 2), ("2", 3, 3), ("3", 3, 4), ("\u00F7", 3, 5), (")", 3, 6), ("cos", 3, 7), ("log2", 3, 8),
    ("C", 4, 2), ("0", 4, 3), ("+", 4, 4), ("^", 4, 5), ("e", 4, 6), ("tan", 4, 7), ("log10", 4, 8),
                                           (".", 5, 5), ("abs", 5, 6), ("_", 5, 7), ("\u27F5", 5, 8),
]

#Iterasi untuk setiap tombol kalkulator
for (char, row, col) in calc_buttons:
    PAD_X, PAD_Y = (1, 1)

    if (col >= 1) and (col <= 6):
        WIDTH = 3; HEIGHT = 1 #Lebar dan tinggi default
    elif col == 8:
        PAD_X, PAD_Y = ((1, 20), 1)
    else:
        WIDTH = 6; HEIGHT = 1

    #Pengaturan fungsi dan tampilan tombol berdasarkan karakter
    if char == "C":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BUTTON_COLOR_2, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda: clicked_entry.delete(0, tk.END)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "e":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = "exp()": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)                
    elif char == "\u221A": #tombol akar kuadrat
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = "sqrt()": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "abs":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = "abs()": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "\u03C0": #tombol 'pi'
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = "\u03C0": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == ".":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10, "bold"), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = char: insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "_":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BUTTON_COLOR_3, relief  = "groove", cursor = "hand2",
                command = lambda t = "\u0020": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "\u27F5": #tombol backspace
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BUTTON_COLOR_3, relief  = "groove", cursor = "hand2",
                command = backspace).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif (row > 1) and ((col == 7) or (col == 8)):
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = char + "()": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    else:
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = char: insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)

#Tombol run untuk menjalankan fungsi perhitungan
run_button = tk.Button(interface, text = "Run", padx = 6, command = output_processing, font = ("Arial", 8, "bold"))
run_button.config(bg = BUTTON_COLOR_1, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
run_button.grid(padx = (20, 0), pady = (12, 0), row = 6, column = 0)

#Label untuk notifikasi error
announce_label = tk.Label(interface, bg = BACKGROUND_COLOR, font = ("Arial", 8), anchor = "w")
announce_label.grid(pady = (10, 0), row = 6, column = 1, sticky = "w")

#Label untuk menampilkan output
output_label = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Output", font = ("Arial", 12, "bold"), anchor = "center")
output_label.grid(padx = (20, 6), pady = (20, 0), row = 7, column = 0)

#Frame tabel hasil
table_frame = tk.Frame(interface)
table_frame.grid(padx = (20, 0), pady = (6, 0), row = 8, column = 0, columnspan = 9)

#Tampilan tabel
style = ttk.Style()
style.configure("Treeview", borderwidth = 2)
style.configure("Treeview.Heading", background = FILL_COLOR, font = ("Arial", 10))

#Scrollbar untuk tabel
scrollbar = ttk.Scrollbar(table_frame, orient = "vertical")
scrollbar.grid(row = 0, column = 1, sticky = "ns")

#Tabel untuk menampilkan iterasi dan perhitungan
table = ttk.Treeview(table_frame, yscrollcommand = scrollbar.set, columns = ("Iterasi", "xi", "g(xi)", "f(xi)"), show = "headings")
table.configure(height = 5)
table.tag_configure("allrows", background = FILL_COLOR)
table.tag_configure("lastrow", background = LASTROW_COLOR)
table.grid(row = 0, column = 0)

#Menghubungkan scrollbar dengan tabel
scrollbar.config(command = table.yview)

#Pengaturan kolom dalam tabel
table.column("#0", width = 0, stretch = tk.NO)
table.column("Iterasi", anchor = tk.CENTER, width = 110)
table.column("xi", anchor = tk.CENTER, width = 110)
table.column("g(xi)", anchor = tk.CENTER, width = 280)
table.column("f(xi)", anchor = tk.CENTER, width = 280)

#Judul untuk tiap kolom
table.heading("#0", text = "", anchor = tk.CENTER)
table.heading("Iterasi", text = "Iterasi", anchor = tk.CENTER)
table.heading("xi", text = "xi", anchor = tk.CENTER)
table.heading("g(xi)", text = "g(xi)", anchor = tk.CENTER)
table.heading("f(xi)", text = "f(xi)", anchor = tk.CENTER)

#Memasukkan data ke dalam tabel
for col, row in enumerate(data):
    if col == (len(data) - 1):
        table.insert(parent = "", index = "end", iid = row[0], text = "", values = row, tags = ("lastrow",))
    else:
        table.insert(parent = "", index = "end", iid = row[0], text = "", values = row, tags = ("allrows",))

#Label hasil akhir
result_label = tk.Label(interface, bg = BACKGROUND_COLOR, text = "x = NULL", font = ("Arial", 8), anchor = "w")
result_label.grid(padx = (20, 0), pady = (0, 6), row = 9, column = 0, sticky = "w")

#Tombol exit
exit_button = tk.Button(interface, text = "Exit", padx = 6, command = interface.destroy, font = ("Arial", 8, "bold"))
exit_button.config(bg = BUTTON_COLOR_2, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
exit_button.grid(padx = (20, 0), pady = (6, 20), row = 10, column = 0)

#Tombol untuk menampilkan plot
plot_button = tk.Button(interface, text = "Show Plots", padx = 6, command = plot, font = ("Arial", 8, "bold"))
plot_button.config(bg = BUTTON_COLOR_1, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
plot_button.grid(padx = (0, 0), pady = (6, 20), row = 10, column = 1, sticky = "w")

interface.mainloop()
