import tkinter as tk
from numpy import *
import matplotlib
import os

def convert_function(input_func):
    input_func = input_func.replace("^", "**").replace("x", "*x")
    input_func = input_func.replace("e", "exp(1)").replace("\u03C0", "pi")
    input_func = input_func.replace("\u00D7", "*").replace("\u00F7", "/")

    final_func = input_func.lstrip("*")

    return final_func

def insert_func_value(func_input, x):
    func = convert_function(func_input)

    try:
        result = float(eval(func))
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

def on_entry_click(event):
    global clicked_entry

    clicked_entry = event.widget

def insert_symbol(symbol):
    cursor_position = clicked_entry.index(tk.INSERT)

    clicked_entry.insert(cursor_position, symbol)

def backspace():
    current_string = clicked_entry.get()

    if current_string:
        new_string = current_string[:-1]

        clicked_entry.delete(0, tk.END)
        clicked_entry.insert(0, new_string)

def hide_label(label):
    label.config(text = "")

def output_processing():
    global func_fx , func_gx, first_x, N_iter, error

    try:
        func_fx = entry_fx.get()
        func_gx = entry_gx.get()
        first_x = entry_x1.get()
        N_iter = entry_N_iter.get()
        error = entry_error.get()

        fx = insert_func_value(func_fx, first_x)
        gx = insert_func_value(func_gx, first_x)

        announce_label.config(text = "Success")
        interface.after(2000, hide_label, announce_label)
    except Exception as e:
        announce_label.config(text = e)
        interface.after(2000, hide_label, announce_label)

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

entry_N_iter = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_N_iter.grid(padx = (12, 20), pady = (8, 0), row = 4, column = 1, sticky = "w")

entry_error = tk.Entry(interface, bg = FILL_COLOR, borderwidth = 1, width = 64, relief = "groove")
entry_error.grid(padx = (12, 20), pady = (8, 0), row = 5, column = 1, sticky = "w")

entry_fx.bind("<Button-1>", on_entry_click)
entry_gx.bind("<Button-1>", on_entry_click)
entry_x1.bind("<Button-1>", on_entry_click)
entry_N_iter.bind("<Button-1>", on_entry_click)
entry_error.bind("<Button-1>", on_entry_click)

calc_buttons = [
    ("7", 1, 2), ("8", 1, 3), ("9", 1, 4), ("-", 1, 5), ("\u221A", 1, 6), ("\u03C0", 1, 7), ("x", 1, 8),
    ("4", 2, 2), ("5", 2, 3), ("6", 2, 4), ("\u00D7", 2, 5), ("(", 2, 6), ("sin", 2, 7), ("log", 2, 8),
    ("1", 3, 2), ("2", 3, 3), ("3", 3, 4), ("\u00F7", 3, 5), (")", 3, 6), ("cos", 3, 7), ("log2", 3, 8),
    ("C", 4, 2), ("0", 4, 3), ("+", 4, 4), ("^", 4, 5), ("e", 4, 6), ("tan", 4, 7), ("log10", 4, 8),
                                                        (".", 5, 6), ("_", 5, 7), ("\u27F5", 5, 8),
]

for (char, row, col) in calc_buttons:
    PAD_X, PAD_Y = (1, 1)

    if (col >= 1) and (col <= 6):
        WIDTH = 3; HEIGHT = 1
    elif col == 8:
        PAD_X, PAD_Y = ((0, 20), 1)
    else:
        WIDTH = 6; HEIGHT = 1

    if char == "C":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda: clicked_entry.delete(0, tk.END)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "\u221A":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = "sqrt()": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "\u03C0":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = "\u03C0": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "_":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = "\u0020": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif char == "\u27F5":
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = backspace).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    elif (row > 1) and ((col == 7) or (col == 8)):
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = char + "()": insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)
    else:
        tk.Button(interface, text = char, width = WIDTH, height = HEIGHT, font = ("Arial", 10), 
                bg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2",
                command = lambda t = char: insert_symbol(t)).grid(padx = PAD_X, pady = PAD_Y, row = row, column = col)

run_button = tk.Button(interface, text = "Run", padx = 6, command = output_processing, font = ("Arial", 8, "bold"))
run_button.config(bg = BUTTON_COLOR_1, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
run_button.grid(padx = (20, 0), pady = (12, 0), row = 6, column = 0)

announce_label = tk.Label(interface, bg = BACKGROUND_COLOR, font = ("Arial", 8, "bold"), anchor = "w")
announce_label.grid(pady = (10, 0), row = 6, column = 1, sticky = "w")

output_label = tk.Label(interface, bg = BACKGROUND_COLOR, text = "Output", font = ("Arial", 12, "bold"), anchor = "center")
output_label.grid(padx = (20, 6), pady = (20, 0), row = 7, column = 0)

exit_button = tk.Button(interface, text = "Exit", padx = 6, command = interface.destroy, font = ("Arial", 8, "bold"))
exit_button.config(bg = BUTTON_COLOR_2, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
exit_button.grid(padx = (20, 0), pady = (6, 20), row = 8, column = 0)

plot_button = tk.Button(interface, text = "Show Plot", padx = 6, command = plot, font = ("Arial", 8, "bold"))
plot_button.config(bg = BUTTON_COLOR_1, fg = BACKGROUND_COLOR, relief  = "groove", cursor = "hand2")
plot_button.grid(padx = (0, 0), pady = (6, 20), row = 8, column = 1, sticky = "w")

interface.mainloop()