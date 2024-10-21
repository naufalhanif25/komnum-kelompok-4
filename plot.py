import matplotlib.pyplot as plt

def plot(x_final, data):
    # Plotting hasil
    plt.figure(figsize=(10, 6))

    # Plot nilai x sepanjang iterasi
    plt.plot(data['Iterasi'], data['x'], label='x', marker='o', color='blue')
    plt.plot(data['Iterasi'], data['F(x)'], label='F(x)', marker='x', color='green')
    plt.plot(data['Iterasi'], data['G(x)'], label='G(x)', marker='^', color='orange')

    # Menambahkan judul dan label
    plt.title('Hasil Iterasi Titik Tetap')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai')
    plt.yscale('linear')
    plt.grid()
    plt.legend()
    
    #Menampilkan plot
    plt.show()
    