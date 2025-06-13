# Tessellation MathCraft: Seed Growth and Sequences

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.patches import RegularPolygon

# -- SECTION 1: a_n as the seed and growth stage --
stages = list(range(1, 6))
a_n = [6*(n-1) for n in stages]  # hexagons added per stage

fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for i, ax in enumerate(axes):
    stage = i + 1
    ax.set_title(f"Stage {stage}\n$a_{stage} = {a_n[i]}")
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    if stage == 1:
        hex_centers = [(0, 0)]
    else:
        hex_centers = [(0, 0)]
        r = stage - 1
        for j in range(6):
            for k in range(r):
                angle = j * np.pi/3
                x = r * np.cos(angle) - k * np.sin(angle)
                y = r * np.sin(angle) + k * np.cos(angle)
                hex_centers.append((x, y))

    for (x, y) in hex_centers:
        hex = RegularPolygon((x, y), numVertices=6, radius=1, orientation=np.pi / 6,
                             facecolor='gold' if (x, y) == (0, 0) else 'lightblue',
                             edgecolor='black')
        ax.add_patch(hex)

plt.suptitle("Visualizing $a_n$ as the Tessellation Seed and Growth", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# -- SECTION 2: Sigma Notation Growth --
df = pd.DataFrame({'Stage': stages, 'a_n': a_n})
df['T_n'] = df['a_n'].cumsum() + 1  # include the center seed

sns.set(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.barplot(x='Stage', y='a_n', data=df, color='skyblue')
plt.title("Sigma Notation as Accumulated Growth: $T_n = 1 + \\sum_{k=1}^{n-1} 6k$", fontsize=14)
plt.xlabel("Stage (n)")
plt.ylabel("Hexagons Added ($a_n$)")
plt.show()

# -- SECTION 3: Triangle Tree Tessellation Problem (structure only for expansion) --
# Triangle pattern: 1, 4, 10, 19, 31 ...
# b_n = 3(n - 1), B_n = 1 + 3(1 + 2 + ... + (n - 1)) = 1 + 3(n-1)n/2

def triangle_tree_total(n):
    return 1 + 3 * (n - 1) * n // 2

def triangle_tree_added(n):
    return 3 * (n - 1)

triangle_df = pd.DataFrame({
    'Stage': list(range(1, 11)),
    'b_n': [triangle_tree_added(n) for n in range(1, 11)],
    'B_n': [triangle_tree_total(n) for n in range(1, 11)]
})

# Visualize Triangle Tree total triangles
plt.figure(figsize=(10, 5))
sns.lineplot(x='Stage', y='B_n', data=triangle_df, marker='o')
plt.title("Triangle Tree Tessellation: Total Triangles per Stage")
plt.xlabel("Stage")
plt.ylabel("Total Triangles ($B_n$)")
plt.grid(True)
plt.show()
