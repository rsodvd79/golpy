import pygame
import numpy as np
import sys
from typing import Tuple

class GameOfLife:
    """
    Implementazione del Game of Life di Conway usando pygame per la visualizzazione.
    """
    
    def __init__(self, width: int = 800, height: int = 600, cell_size: int = 10):
        """
        Inizializza il Game of Life.
        
        Args:
            width: Larghezza della finestra in pixel
            height: Altezza della finestra in pixel  
            cell_size: Dimensione di ogni cella in pixel
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        
        # Calcola il numero di celle nella griglia
        self.grid_width = width // cell_size
        self.grid_height = height // cell_size
        
        # Inizializza pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game of Life (Griglia Toroidale) - Premi SPAZIO per pausa, R per reset, C per cancellare")
        self.clock = pygame.time.Clock()
        
        # Colori
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.GRAY = (128, 128, 128)
        
        # Stato del gioco
        self.grid = np.zeros((self.grid_height, self.grid_width), dtype=int)
        self.running = True
        self.paused = True
        
        # Inizializza con un pattern interessante
        self.initialize_glider()
        
    def initialize_glider(self):
        """
        Inizializza la griglia con pattern che dimostrano la griglia toroidale.
        """
        # Glider pattern al centro
        glider = np.array([
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ])
        
        center_row = self.grid_height // 2
        center_col = self.grid_width // 2
        self.grid[center_row:center_row+3, center_col:center_col+3] = glider
        
        # Glider vicino al bordo destro per dimostrare il wrapping
        edge_col = self.grid_width - 2
        self.grid[center_row:center_row+3, edge_col:edge_col+2] = glider[:, :2]
        self.grid[center_row:center_row+3, 0:1] = glider[:, 2:3]  # Parte che "avvolge"
        
        # Oscillatore (blinker) vicino al bordo inferiore
        blinker = np.array([[1, 1, 1]])
        bottom_row = self.grid_height - 1
        self.grid[bottom_row:bottom_row+1, center_col:center_col+3] = blinker
        
        # Piccolo oscillatore che attraversa il bordo superiore/inferiore
        vertical_blinker = np.array([[1], [1], [1]])
        self.grid[self.grid_height-1:self.grid_height, 10:11] = vertical_blinker[:1, :]
        self.grid[0:2, 10:11] = vertical_blinker[1:, :]
        
    def get_neighbors_count(self, row: int, col: int) -> int:
        """
        Conta il numero di vicini vivi per una cella specifica.
        Implementa una griglia toroidale: i bordi opposti sono connessi.
        
        Args:
            row: Riga della cella
            col: Colonna della cella
            
        Returns:
            Numero di vicini vivi
        """
        count = 0
        
        # Controlla tutte le 8 direzioni
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:  # Salta la cella corrente
                    continue
                    
                # Calcola le coordinate con wrapping toroidale
                # L'operazione modulo % crea l'effetto di bordi infiniti
                new_row = (row + dr) % self.grid_height
                new_col = (col + dc) % self.grid_width
                
                # Non serve più verificare i confini grazie al modulo
                count += self.grid[new_row, new_col]
                    
        return count
    
    def update_grid(self):
        """
        Aggiorna la griglia secondo le regole del Game of Life.
        
        Regole:
        1. Una cella viva con 2 o 3 vicini vivi sopravvive
        2. Una cella morta con esattamente 3 vicini vivi diventa viva
        3. Tutte le altre celle muoiono o rimangono morte
        """
        new_grid = np.zeros_like(self.grid)
        
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                neighbors = self.get_neighbors_count(row, col)
                
                if self.grid[row, col] == 1:  # Cella viva
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row, col] = 1
                else:  # Cella morta
                    if neighbors == 3:
                        new_grid[row, col] = 1
                        
        self.grid = new_grid
    
    def draw_grid(self):
        """
        Disegna la griglia sullo schermo.
        """
        self.screen.fill(self.BLACK)
        
        # Disegna le celle
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                x = col * self.cell_size
                y = row * self.cell_size
                
                if self.grid[row, col] == 1:
                    pygame.draw.rect(self.screen, self.GREEN, 
                                   (x, y, self.cell_size, self.cell_size))
                
                # Disegna le linee della griglia (opzionale)
                pygame.draw.rect(self.screen, self.GRAY, 
                               (x, y, self.cell_size, self.cell_size), 1)
    
    def handle_mouse_click(self, pos: Tuple[int, int]):
        """
        Gestisce i click del mouse per attivare/disattivare le celle.
        
        Args:
            pos: Posizione del click (x, y)
        """
        x, y = pos
        col = x // self.cell_size
        row = y // self.cell_size
        
        if 0 <= row < self.grid_height and 0 <= col < self.grid_width:
            self.grid[row, col] = 1 - self.grid[row, col]  # Inverti lo stato
    
    def clear_grid(self):
        """
        Cancella tutte le celle dalla griglia.
        """
        self.grid = np.zeros((self.grid_height, self.grid_width), dtype=int)
    
    def randomize_grid(self, probability: float = 0.3):
        """
        Riempie la griglia casualmente.
        
        Args:
            probability: Probabilità che una cella sia viva
        """
        self.grid = np.random.choice([0, 1], size=(self.grid_height, self.grid_width), 
                                   p=[1-probability, probability])
    
    def run(self):
        """
        Loop principale del gioco.
        """
        print("=== GAME OF LIFE TOROIDALE ===")
        print("La griglia è toroidale: i bordi opposti sono connessi!")
        print("I pattern che escono da un lato riappaiono dall'altro.")
        print("")
        print("Controlli:")
        print("SPAZIO - Pausa/Riprendi")
        print("R - Reset con pattern iniziale")
        print("C - Cancella griglia")
        print("T - Riempimento casuale")
        print("Click mouse - Attiva/disattiva cella")
        print("ESC - Esci")
        print("")
        print("Osserva come i glider attraversano i bordi!")
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                        print(f"Gioco {'in pausa' if self.paused else 'ripreso'}")
                        
                    elif event.key == pygame.K_r:
                        self.clear_grid()
                        self.initialize_glider()
                        self.paused = True
                        print("Griglia resettata")
                        
                    elif event.key == pygame.K_c:
                        self.clear_grid()
                        print("Griglia cancellata")
                        
                    elif event.key == pygame.K_t:
                        self.randomize_grid()
                        print("Griglia riempita casualmente")
                        
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Click sinistro
                        self.handle_mouse_click(event.pos)
            
            # Aggiorna il gioco solo se non è in pausa
            if not self.paused:
                self.update_grid()
            
            # Disegna tutto
            self.draw_grid()
            pygame.display.flip()
            
            # Limita i FPS
            self.clock.tick(10)  # 10 FPS per vedere meglio l'evoluzione
        
        pygame.quit()
        sys.exit()

def main():
    """
    Funzione principale per avviare il Game of Life.
    """
    print("Avvio del Game of Life con griglia toroidale...")
    print("Caricamento della finestra pygame...")
    print("La griglia è ora virtualmente infinita - i bordi si connettono!")
    
    # Crea e avvia il gioco
    game = GameOfLife(width=1000, height=700, cell_size=8)
    game.run()

if __name__ == "__main__":
    main()

