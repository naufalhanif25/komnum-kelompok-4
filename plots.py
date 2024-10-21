import matplotlib.pyplot as plt

#Fungsi untuk menampilkan grafik 
def plots(final_x, data):
    GRAPH_1 = "#ECCC68"
    GRAPH_2 = "#2ED573"
    GRAPH_3 = "#00A8FF"
    DOT = "#FF4757"
    
    N_list = [sliced_col for col in data for sliced_col in col[0]]
    x_list = [sliced_col for col in data for sliced_col in col[1]]
    gx_list = [sliced_col for col in data for sliced_col in col[2]]
    fx_list = [sliced_col for col in data for sliced_col in col[3]]
    
    window = plt.figure(figsize = (6, 4))
    window.canvas.manager.set_window_title("Plots")

    #Membuat plot untuk x_list, gx_list, dan fx_list terhadap N_list
    plt.plot(N_list, x_list, label = "x", marker = "o", color = GRAPH_1)
    plt.plot(N_list, gx_list, label = "g(x)", marker = "^", color = GRAPH_2)
    plt.plot(N_list, fx_list, label = "f(x)", marker = "x", color = GRAPH_3)
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)

    #Menambahkan judul dan label pada sumbu grafik
    plt.xlabel("Iterasi", fontsize = 8, fontweight = "bold")
    plt.ylabel("X", fontsize = 8, fontweight = "bold")
    plt.yscale("linear")
    plt.grid(True)
    plt.plot(N_list[len(N_list) - 1], final_x, "r*", label = f"x = {final_x:.5f}", color = DOT)
    plt.legend(fontsize = 8)
    plt.text(N_list[len(N_list) - 1] - 1.5, final_x + 0.35, f"x = {final_x:.5f}", fontsize = 8, bbox = dict(facecolor = GRAPH_1, alpha = 0.25))
    
    plt.show() #Menampilkan grafik
