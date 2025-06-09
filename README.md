# Game of Life con Pygame (Griglia Toroidale)

Un'implementazione completa del famoso "Game of Life" di John Conway utilizzando Python e pygame per la visualizzazione grafica. Questa versione implementa una **griglia toroidale** che rende l'universo virtualmente infinito.

## Descrizione

Il Game of Life è un automa cellulare ideato dal matematico britannico John Conway nel 1970. È un "gioco" a zero giocatori, il che significa che la sua evoluzione è determinata dal suo stato iniziale, senza richiedere ulteriori input.

### Regole del Game of Life

1. **Sopravvivenza**: Una cella viva con 2 o 3 vicini vivi sopravvive alla generazione successiva
2. **Nascita**: Una cella morta con esattamente 3 vicini vivi diventa viva
3. **Morte**: Tutte le altre celle muoiono per isolamento o sovrappopolazione

## Caratteristiche del Programma

- **Griglia toroidale**: I bordi opposti sono connessi, creando un universo infinito
- **Visualizzazione grafica**: Griglia interattiva con pygame
- **Controlli intuitivi**: Mouse e tastiera per interagire
- **Pattern predefiniti**: Pattern posizionati strategicamente per dimostrare il wrapping
- **Modalità interattiva**: Possibilità di disegnare pattern personalizzati
- **Generazione casuale**: Riempimento casuale della griglia
- **Effetto wrapping**: I pattern che escono da un lato riappaiono dall'altro

## Installazione

1. Assicurati di avere Python 3.7+ installato
2. Clona o scarica questo progetto
3. Naviga nella directory del progetto:
   ```bash
   cd /gol
   ```
4. Attiva l'ambiente virtuale:
   ```bash
   source venv/bin/activate
   ```
5. Installa le dipendenze (se non già fatto):
   ```bash
   pip install pygame numpy
   ```

## Utilizzo

Per avviare il programma:

```bash
source venv/bin/activate
python game_of_life_pygame.py
```

### Controlli

| Tasto/Azione | Funzione |
|--------------|----------|
| **SPAZIO** | Pausa/Riprendi la simulazione |
| **R** | Reset con pattern iniziale (glider + blinker) |
| **C** | Cancella tutta la griglia |
| **T** | Riempimento casuale della griglia |
| **Click sinistro** | Attiva/disattiva una cella specifica |
| **ESC** | Esci dal programma |
| **X (finestra)** | Chiudi il programma |

## Pattern Interessanti

Il programma inizia con due pattern classici:

### Glider
Un pattern che si muove diagonalmente attraverso la griglia:
```
.X.
X.X
XXX
```

### Blinker (Oscillatore)
Un pattern che oscilla tra due stati:
```
XXX  →  .X.  →  XXX
        .X.
        .X.
```

## Struttura del Codice

### Classe GameOfLife

- `__init__()`: Inizializza pygame e imposta la griglia
- `get_neighbors_count()`: Conta i vicini vivi di una cella
- `update_grid()`: Applica le regole del Game of Life
- `draw_grid()`: Renderizza la griglia sullo schermo
- `handle_mouse_click()`: Gestisce l'interazione con il mouse
- `run()`: Loop principale del gioco

### Funzioni di Utilità

- `clear_grid()`: Cancella tutte le celle
- `randomize_grid()`: Riempie casualmente la griglia
- `initialize_glider()`: Imposta pattern predefiniti

## Personalizzazione

Puoi modificare facilmente:

- **Dimensioni finestra**: Modifica `width` e `height` nella funzione `main()`
- **Dimensione celle**: Cambia `cell_size` per celle più grandi o piccole
- **Velocità**: Modifica il valore in `clock.tick()` per cambiare la velocità
- **Colori**: Cambia i valori RGB nelle costanti di colore
- **Pattern iniziali**: Modifica la funzione `initialize_glider()`

## Esempi di Utilizzo

1. **Osservazione**: Avvia il programma e premi SPAZIO per vedere l'evoluzione dei pattern
2. **Creazione**: Premi C per cancellare, poi clicca per creare il tuo pattern
3. **Sperimentazione**: Premi T per pattern casuali e osserva cosa emerge

## Requisiti Tecnici

- Python 3.7+
- pygame 2.0+
- numpy 1.19+
- Sistema operativo: macOS, Windows, Linux

## Note Tecniche

- **Griglia toroidale**: I confini si "avvolgono" usando l'operazione modulo (%)
- **Topologia toroidale**: Il bordo destro si connette al sinistro, il superiore all'inferiore
- **Algoritmo ottimizzato**: Calcolo dei vicini con wrapping automatico
- **Implementazione efficiente**: Usa numpy per operazioni matriciali veloci
- Frame rate impostato a 10 FPS per visualizzazione ottimale

## Griglia Toroidale

### Cos'è una griglia toroidale?
Una griglia toroidale è una superficie che si "avvolge" su se stessa, come un toroide (ciambella). In pratica:

- Il **bordo destro** si connette al **bordo sinistro**
- Il **bordo superiore** si connette al **bordo inferiore**
- Un pattern che esce da un lato riappare immediatamente dall'altro
- Non esistono più "bordi morti" che influenzano l'evoluzione

### Vantaggi della griglia toroidale:
- **Universo infinito**: I pattern possono evolvere senza limitazioni di confine
- **Comportamento naturale**: I glider continuano a muoversi indefinitamente
- **Simmetria perfetta**: Tutti i punti della griglia hanno le stesse proprietà
- **Pattern stabili**: Oscillatori e strutture non vengono disturbati dai bordi

### Esempi visibili:
- I **glider** attraversano i bordi e continuano dall'altra parte
- Gli **oscillatori** ai bordi mantengono la loro periodicità
- I **pattern casuali** creano effetti di continuità sorprendenti

## Possibili Estensioni

- Salvataggio e caricamento di pattern
- Statistiche sulla popolazione
- Pattern library con forme famose
- Modalità step-by-step
- Zoom e pan sulla griglia
- Visualizzazione 3D del toroide

Esplora l'universo infinito del Game of Life toroidale! 🌍🎮

**Prova questo:** Avvia il programma, premi SPAZIO e osserva come i glider attraversano i bordi della schermata per riapparire dall'altra parte. È affascinante vedere come l'assenza di confini cambi completamente il comportamento dei pattern!

