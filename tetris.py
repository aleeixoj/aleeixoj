import random

grid_size = (10, 20)  # 10 colunas x 20 linhas

tetris_pieces = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

green_shades = ["🟩", "🟨", "🟩", "🟦", "🟩"]  # Vários tons de verde
empty_cell = "⬛"

def place_piece(board, piece):
    piece_color = random.choice(green_shades)
    start_col = random.randint(0, grid_size[0] - len(piece[0]))
    start_row = random.randint(0, grid_size[1] - len(piece))
    
    for r in range(len(piece)):
        for c in range(len(piece[r])):
            if piece[r][c] == 1:
                board[start_row + r][start_col + c] = piece_color

def generate_tetris_board():
    board = [[empty_cell for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for _ in range(5):  # Coloca 5 peças aleatórias
        piece = random.choice(tetris_pieces)
        place_piece(board, piece)
    return board

def board_to_markdown(board):
    return "\n".join(["".join(row) for row in board])

def update_readme():
    with open("README.md", "r") as file:
        content = file.readlines()
    
    start_marker = "<!-- TETRIS-GRID-START -->"
    end_marker = "<!-- TETRIS-GRID-END -->"
    
    start_index = content.index(start_marker + "\n") + 1
    end_index = content.index(end_marker + "\n")
    
    board = generate_tetris_board()
    board_md = board_to_markdown(board)
    
    new_content = content[:start_index] + [board_md + "\n"] + content[end_index:]
    
    with open("README.md", "w") as file:
        file.writelines(new_content)

if __name__ == "__main__":
    update_readme()
