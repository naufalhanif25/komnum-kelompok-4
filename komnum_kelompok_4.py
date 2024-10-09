import numpy as np
import tkinter as tk
import matplotlib as plt
import prettytable as pt

def interface():
    interface = tk.Tk()

    tk.Label(interface, text = "Fungsi f(x)").grid(padx = 12, pady = 12, row = 0)

    entry_1 = tk.Entry(interface, width = 64)
    entry_1.grid(row = 0, column = 1)

    tk.Label(interface, text = "Error").grid(padx = 12, pady = 0, row = 1)
    
    entry_2 = tk.Entry(interface, width = 64)
    entry_2.grid(row = 1, column = 1)

    interface.geometry("660x400")
    interface.title("Metode Iterasi")
    interface.iconbitmap("icon.ico")

    interface.mainloop()

def function():
    print("f(x)")

def iteration_method():
    print("Metode iterasi")

def table():
    print("Tabel")

def plot():
    print("Plot")

def main():
    interface()

main()
