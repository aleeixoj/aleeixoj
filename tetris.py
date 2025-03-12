import numpy as np
import imageio
import matplotlib.pyplot as plt
import time

# Configuração do tabuleiro do Tetris
ROWS, COLS = 20, 10
frames = []

# Cores para os blocos
colors = ["black", "red", "blue", "green", "yellow", "purple", "orange", "cyan"]

def generate_frame(board):
    fig, ax = plt.subplots(figsize=(3, 6))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    for r in range(ROWS):
        for c in range(COLS):
            color = colors[board[r, c]]
            ax.add_patch(plt.Rectangle((c, ROWS - r - 1), 1, 1, color=color, ec="gray"))
    
    plt.xlim(0, COLS)
    plt.ylim(0, ROWS)
    
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(image)
    plt.close(fig)

def simulate_tetris():
    board = np.zeros((ROWS, COLS), dtype=int)
    for i in range(10):  # Simula 10 movimentos
        piece_color = np.random.randint(1, len(colors))
        col = np.random.randint(0, COLS - 1)
        board[np.random.randint(0, ROWS), col] = piece_color
        generate_frame(board)
        time.sleep(0.2)  # Simula movimento
    
simulate_tetris()
imageio.mimsave("tetris.gif", frames, duration=0.2)
print("GIF do Tetris gerado!")
