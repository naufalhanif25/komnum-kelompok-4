import numpy as np
import tkinter as tk
import matplotlib as plt
import prettytable as pt

#Fungsi untuk mengonversi fungsi matematika input dari format teks
def convert_function(input_func):
    input_func = input_func.replace("^", "**").replace("x", "*x")
    final_func = input_func.lstrip("*")

    return final_func

def insert_func_value(func_input, x):
    func = convert_function(func_input)

    try:
        result = eval(func)
    except Exception as e:
        print("Error:", e)

    return result

def function():
    print("f(x)")

def iteration_method():
    print("Metode iterasi")

def table():
    print("Tabel")

def plot():
    print("Plot")

def main():
    interface = tk.Tk()

    tk.Label(interface, text = "INPUT", font = ("Arial", 8, "bold")).grid(padx = 12, pady = 6, row = 0)

    tk.Label(interface, text = "Fungsi f(x)").grid(padx = 12, pady = 0, row = 1)
    tk.Label(interface, text = "Fungsi g(x)").grid(padx = 12, pady = 6, row = 2)
    tk.Label(interface, text = "X awal").grid(padx = 12, pady = 0, row = 3)
    tk.Label(interface, text = "Iterasi (N)").grid(padx = 12, pady = 6, row = 4)
    tk.Label(interface, text = "Error").grid(padx = 12, pady = 0, row = 5)

    entry_1 = tk.Entry(interface, width = 64)
    entry_1.grid(row = 1, column = 1)

    entry_2 = tk.Entry(interface, width = 64)
    entry_2.grid(row = 2, column = 1)

    entry_3 = tk.Entry(interface, width = 64)
    entry_3.grid(row = 3, column = 1)

    entry_4 = tk.Entry(interface, width = 64)
    entry_4.grid(row = 4, column = 1)

    entry_5 = tk.Entry(interface, width = 64)
    entry_5.grid(row = 5, column = 1)

    tk.Label(interface, text = "\n", font = "Arial 4").grid(padx = 12, pady = 0, row = 6)

    def get_value():
        func_fx = entry_1.get()
        func_gx = entry_2.get()
        first_x = entry_3.get()
        iter_N = entry_4.get()
        error = entry_5.get()

    button = tk.Button(text = "Run", command = get_value)
    button.grid(padx = 12, pady = 6, row = 7)

    tk.Label(interface, text = "OUTPUT", font = ("Arial", 8, "bold")).grid(padx = 12, pady = 6, row = 8)

    interface.geometry("500x400")
    interface.title("Metode Iterasi")
    interface.iconbitmap("icon.ico")

    interface.mainloop()

main()
