import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Define the board layout and colors
light_square_color = "#F0D9B5"  # light beige
dark_square_color = "#B58863"   # brown
neutral_cmap = ListedColormap([light_square_color, dark_square_color])

# Create the 8x8 alternating pattern
chessboard = np.fromfunction(lambda i, j: (i + j) % 2, (8, 8))

# Define labels for axes
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = list(range(8, 0, -1))

# Define the initial position of the pieces
pieces = {
    "a1": "♖", "b1": "♘", "c1": "♗", "d1": "♕", "e1": "♔", "f1": "♗", "g1": "♘", "h1": "♖",
    "a2": "♙", "b2": "♙", "c2": "♙", "d2": "♙", "e2": "♙", "f2": "♙", "g2": "♙", "h2": "♙",
    "a7": "♟", "b7": "♟", "c7": "♟", "d7": "♟", "e7": "♟", "f7": "♟", "g7": "♟", "h7": "♟",
    "a8": "♜", "b8": "♞", "c8": "♝", "d8": "♛", "e8": "♚", "f8": "♝", "g8": "♞", "h8": "♜",
}

# Create the plot
fig, ax = plt.subplots()
ax.imshow(chessboard, cmap=neutral_cmap)

# Set axis ticks and labels
ax.set_xticks(np.arange(8))
ax.set_yticks(np.arange(8))
ax.set_xticklabels(columns)
ax.set_yticklabels(rows)

# Remove internal gridlines and ticks
ax.set_xticks([], minor=True)
ax.set_yticks([], minor=True)
ax.grid(False)
ax.tick_params(which='both', bottom=False, left=False)

# Draw thick black border around the board
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(2)

# Keep squares square
ax.set_aspect('equal')

# Draw the pieces
for pos, piece in pieces.items():
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    ax.text(col, row, piece, fontsize=28, ha='center', va='center')

plt.show()