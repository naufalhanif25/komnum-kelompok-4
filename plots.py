import matplotlib.pyplot as plt
import pandas as pd

def plots(final_x, data):
    N_list = [sliced_col for col in data for sliced_col in col[0]]
    x_list = [sliced_col for col in data for sliced_col in col[1]]
    gx_list = [sliced_col for col in data for sliced_col in col[2]]
    fx_list = [sliced_col for col in data for sliced_col in col[3]]
    
    plt.figure(figsize = (10, 6))

    plt.plot(N_list, x_list, label = "x", marker = "o", color = "blue")
    plt.plot(N_list, gx_list, label = "g(x)", marker = "^", color = "green")
    plt.plot(N_list, fx_list, label = "f(x)", marker = "x", color = "orange")

    plt.title("Hasil Iterasi")
    plt.xlabel("Iterasi")
    plt.ylabel("Nilai")
    plt.yscale("linear")
    plt.grid(True)
    plt.legend()
    
    plt.show()