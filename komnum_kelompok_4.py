import numpy as np
import tkinter as tk
import matplotlib
import os

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

def output_processing():
    global func_fx , func_gx, first_x, N_iter, error

    func_fx = entry_fx.get()
    func_gx = entry_gx.get()
    first_x = entry_x1.get()
    N_iter = entry_n_iter.get()
    error = entry_error.get()

    fx = insert_func_value(func_fx, first_x)
    gx = insert_func_value(func_gx, first_x)

current_dir = os.path.dirname(__file__)

BACKGROUND_COLOR = "#FFFFFF"
FILL_COLOR = "#F1F2F6"
BUTTON_COLOR_1 = "#00A8FF"
BUTTON_COLOR_2 = "#FF4757"

interface = tk.Tk()
interface.resizable(False, False)
interface.title("Metode Iterasi")
interface.iconbitmap(current_dir + "\\icon.ico")
interface.config(bg = BACKGROUND_COLOR)

input_label = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Input", font = ("Arial", 12, "bold"), anchor = "center")
input_label.grid(padx = (20, 0), pady = (6, 0), row = 0, column = 0)

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

entry_fx = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_fx.grid(padx = (12, 20), pady = (8, 0), row = 1, column = 1, sticky = "w")

entry_gx = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_gx.grid(padx = (12, 20), pady = (8, 0), row = 2, column = 1, sticky = "w")

entry_x1 = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_x1.grid(padx = (12, 20), pady = (8, 0), row = 3, column = 1, sticky = "w")

entry_n_iter = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_n_iter.grid(padx = (12, 20), pady = (8, 0), row = 4, column = 1, sticky = "w")

entry_error = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_error.grid(padx = (12, 20), pady = (8, 0), row = 5, column = 1, sticky = "w")

run_button = tk.Button(interface, text = "Run", padx = 6, command = output_processing, font = ("Arial", 8, "bold"))
run_button.config(bg = BUTTON_COLOR_1, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
run_button.grid(padx = (20, 0), pady = (12, 0), row = 6, column = 0)

output_label = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Output", font = ("Arial", 12, "bold"), anchor = "center")
output_label.grid(padx = (20, 6), pady = (20, 0), row = 7, column = 0)

exit_button = tk.Button(interface, text = "Exit", padx = 6, command = interface.destroy, font = ("Arial", 8, "bold"))
exit_button.config(bg = BUTTON_COLOR_2, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
exit_button.grid(padx = (20, 0), pady = (6, 20), row = 8, column = 0)

plot_button = tk.Button(interface, text = "Show Plot", padx = 6, command = plot, font = ("Arial", 8, "bold"))
plot_button.config(bg = BUTTON_COLOR_1, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
plot_button.grid(padx = (0, 0), pady = (6, 20), row = 8, column = 1, sticky = "w")

interface.mainloop()