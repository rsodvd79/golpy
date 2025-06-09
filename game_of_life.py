import numpy as np
import time
import os
import matplotlib.pyplot as plt

# Parametri della griglia
dim_x = 20
dim_y = 40

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def stampa_griglia(griglia):
    for riga in griglia:
        print(''.join(['█' if cella else ' ' for cella in riga]))

def mostra_griglia(griglia):
    plt.imshow(griglia, cmap='binary')
    plt.axis('off')
    plt.pause(0.1)
    plt.clf()

def aggiorna_griglia(griglia):
    nuova_griglia = np.zeros((dim_x, dim_y), dtype=int)
    for i in range(dim_x):
        for j in range(dim_y):
            # Somma dei vicini
            vicini = np.sum(griglia[max(0,i-1):min(i+2,dim_x), max(0,j-1):min(j+2,dim_y)]) - griglia[i,j]
            # Regole del Game of Life
            if griglia[i,j] == 1 and (vicini == 2 or vicini == 3):
                nuova_griglia[i,j] = 1
            elif griglia[i,j] == 0 and vicini == 3:
                nuova_griglia[i,j] = 1
    return nuova_griglia

def main():
    # Inizializzazione casuale
    griglia = np.random.choice([0, 1], size=(dim_x, dim_y))
    plt.ion()
    plt.figure(figsize=(10, 5))
    while True:
        mostra_griglia(griglia)
        griglia = aggiorna_griglia(griglia)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
