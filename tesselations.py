# Tessellation MathCraft: Seed Growth and Sequences (Enhanced Streamlit App)

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sympy as sp
from matplotlib.patches import RegularPolygon

# -- Streamlit Page Setup --
st.set_page_config(page_title="MathCraft: Tessellations", layout="wide")
st.title("🌱 MathCraft: Seed Tessellation & Sequences")

# -- SECTION 1: a_n as the seed and growth stage --
st.header("1️⃣ Visualizing $a_n$ as Seed Growth")
stages = list(range(1, 6))
a_n = [6*(n-1) for n in stages]  # hexagons added per stage

fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for i, ax in enumerate(axes):
    stage = i + 1
    ax.set_title(f"Stage {stage}\n" + r"$a_{{{}}} = {}$".format(stage, a_n[i]))
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
st.pyplot(fig)

# -- SECTION 2: Sigma Notation Growth --
st.header("2️⃣ Understanding $\Sigma$ as Accumulated Growth")
df = pd.DataFrame({'Stage': stages, 'a_n': a_n})
df['T_n'] = df['a_n'].cumsum() + 1  # include the center seed

fig2 = plt.figure(figsize=(10, 5))
sns.barplot(x='Stage', y='a_n', data=df, color='skyblue')
plt.title("Sigma Notation as Accumulated Growth: $T_n = 1 + \sum_{k=1}^{n-1} 6k$", fontsize=14)
plt.xlabel("Stage (n)")
plt.ylabel("Hexagons Added ($a_n$)")
st.pyplot(fig2)

# -- SECTION 3: Triangle Tree Tessellation --
st.header("🌲 Triangle Tree Tessellation & Sequence Tutorial")
def triangle_tree_total(n):
    return 1 + 3 * (n - 1) * n // 2

def triangle_tree_added(n):
    return 3 * (n - 1)

triangle_df = pd.DataFrame({
    'Stage': list(range(1, 11)),
    'b_n': [triangle_tree_added(n) for n in range(1, 11)],
    'B_n': [triangle_tree_total(n) for n in range(1, 11)]
})

fig3 = plt.figure(figsize=(10, 5))
sns.lineplot(x='Stage', y='B_n', data=triangle_df, marker='o')
plt.title("Triangle Tree Tessellation: Total Triangles per Stage")
plt.xlabel("Stage")
plt.ylabel("Total Triangles ($B_n$)")
plt.grid(True)
st.pyplot(fig3)

# -- SECTION 4: Interactive Sequence Calculators --
st.header("🧮 Interactive Sequence Calculators")

st.subheader("🔷 Hexagon Sequence Calculator")
hex_stage = st.slider("Choose stage for hexagon tessellation:", 1, 25, 5)
hex_an = 6 * (hex_stage - 1)
hex_Tn = 1 + 3 * hex_stage * (hex_stage - 1)
st.latex(f"a_{{{hex_stage}}} = {hex_an}")
st.latex(f"T_{{{hex_stage}}} = 1 + 3({hex_stage})({hex_stage - 1}) = {hex_Tn}")

st.subheader("🔺 Triangle Tree Calculator")
tri_stage = st.slider("Choose stage for triangle tessellation:", 1, 25, 5)
tri_bn = 3 * (tri_stage - 1)
tri_Bn = 1 + 3 * (tri_stage - 1) * tri_stage // 2
st.latex(f"b_{{{tri_stage}}} = {tri_bn}")
st.latex(f"B_{{{tri_stage}}} = 1 + 3 * (n-1)n/2 = {tri_Bn}")

st.markdown("""
**Key Terms:**  
- $n$: The growth stage (starts at 1, includes the seed)  
- $k$: The ring or level around the seed (used in sigma notation)  
- $a_n$: Hexagons added at stage $n$  
- $T_n$: Total number of hexagons at stage $n$  
- $b_n$: Triangles added at stage $n$  
- $B_n$: Total number of triangles at stage $n$

**Challenge:** Can you create a custom tessellation rule and sequence?
""")
