import matplotlib.pyplot as plt
import pandas as pd

def plot(x_final, data):
    #Membuat dataframe
    df = pd.DataFrame(data, columns=['Iterasi', 'x', 'F(x)', 'G(x)'])
    
    # Plotting hasil
    plt.figure(figsize=(10, 6))

    # Plot nilai x sepanjang iterasi
    plt.plot(df['Iterasi'], df['x'], label='x', marker='o', color='blue')
    plt.plot(df['Iterasi'], df['F(x)'], label='F(x)', marker='x', color='green')
    plt.plot(df['Iterasi'], df['G(x)'], label='G(x)', marker='^', color='orange')

    # Menambahkan judul dan label
    plt.title('Hasil Iterasi Titik Tetap')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai')
    plt.yscale('linear')
    plt.grid()
    plt.legend()
    plt.show()
    