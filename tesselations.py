# MathCraft: Seed Tessellations - From One to Many 🌱
# Complete tutorial with visual associations for sequences and tessellations

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.patches import RegularPolygon
import matplotlib.patches as patches

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("🌱 MathCraft: Seed Tessellations - From One to Many")
print("=" * 60)

# =============================================================================
# SECTION 1: Visualizing a_n as SEED GROWTH 🌱
# =============================================================================

def generate_hex_centers(stage):
    """Generate hexagon centers for a given stage in hexagonal tessellation"""
    if stage == 1:
        return [(0, 0)]
    
    centers = [(0, 0)]  # Seed hexagon at center
    
    # Add rings around the center
    for ring in range(1, stage):
        # Each ring has 6 * ring hexagons
        for i in range(6 * ring):
            # Calculate angle and position
            if ring == 1:
                angle = i * (2 * np.pi / 6)
                x = ring * 1.5 * np.cos(angle)
                y = ring * 1.5 * np.sin(angle)
            else:
                # For outer rings, distribute evenly around perimeter
                angle = i * (2 * np.pi / (6 * ring))
                x = ring * 1.5 * np.cos(angle)
                y = ring * 1.5 * np.sin(angle)
            centers.append((x, y))
    
    return centers

# Create visualization of seed concept
fig, axes = plt.subplots(1, 5, figsize=(25, 5))
stages = list(range(1, 6))

for i, ax in enumerate(axes):
    stage = i + 1
    a_n = 6 * (stage - 1)  # New hexagons added at this stage
    
    ax.set_title(f"Stage {stage}\n$a_{stage} = 6({stage}-1) = {a_n}$\n{'SEED' if stage == 1 else f'New Ring: {a_n} hexagons'}", 
                 fontsize=12, fontweight='bold')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Generate hex centers for this stage
    hex_centers = generate_hex_centers(stage)
    
    # Draw hexagons
    for j, (x, y) in enumerate(hex_centers):
        # Color: gold for seed, different colors for each ring
        if j == 0:  # Seed hexagon
            color = 'gold'
            edge_width = 3
        elif stage == 2 and j <= 6:  # First ring
            color = 'lightcoral'
            edge_width = 2
        elif stage == 3 and j > 6:  # Second ring  
            color = 'lightblue'
            edge_width = 2
        elif stage == 4 and j > 18:  # Third ring
            color = 'lightgreen'
            edge_width = 2
        elif stage == 5 and j > 36:  # Fourth ring
            color = 'plum'
            edge_width = 2
        else:
            color = 'lightgray'
            edge_width = 1
            
        hex_poly = RegularPolygon((x, y), numVertices=6, radius=0.7, 
                                 orientation=np.pi/6, facecolor=color, 
                                 edgecolor='black', linewidth=edge_width)
        ax.add_patch(hex_poly)

plt.suptitle("🌱 SEED CONCEPT: $a_n = 6(n-1)$ represents NEW hexagons added at stage n", 
             fontsize=16, fontweight='bold', y=0.95)
plt.tight_layout()
plt.show()

print("\n📖 MATHEMATICAL INTERPRETATION:")
print("• n = growth stage from seed")
print("• a_n = new hexagons added at stage n")
print("• Stage 1: a_1 = 0 (just the seed, no new hexagons)")
print("• Stage 2: a_2 = 6 (first ring around seed)")
print("• Stage 3: a_3 = 12 (second ring)")
print("• Pattern: Each ring adds 6 more hexagons than the previous ring")

# =============================================================================
# SECTION 2: Sigma (Σ) as ACCUMULATED GROWTH 📊
# =============================================================================

print("\n" + "="*60)
print("🔢 SIGMA NOTATION: Accumulated Growth")
print("="*60)

# Create data for visualization
stages_extended = list(range(1, 11))
a_n_values = [6*(n-1) for n in stages_extended]
T_n_values = [1 + sum(a_n_values[:i]) for i in range(len(stages_extended))]

# Create comprehensive dataframe
df = pd.DataFrame({
    'Stage (n)': stages_extended,
    'New Added (a_n)': a_n_values,
    'Total (T_n)': T_n_values,
    'k_values': [f"k=1 to {n-1}" if n > 1 else "none" for n in stages_extended]
})

print(df.head(8))

# Visualization of Sigma concept
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Left plot: Individual contributions (a_n)
bars1 = ax1.bar(df['Stage (n)'][:8], df['New Added (a_n)'][:8], 
                color=['gold' if i == 0 else 'lightblue' for i in range(8)], 
                edgecolor='black', linewidth=1)
ax1.set_title('$a_n = 6(n-1)$: New Hexagons Added per Stage', fontsize=14, fontweight='bold')
ax1.set_xlabel('Stage (n)')
ax1.set_ylabel('New Hexagons Added')
ax1.grid(True, alpha=0.3)

# Add value labels on bars
for i, bar in enumerate(bars1):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

# Right plot: Cumulative total (T_n)
line = ax2.plot(df['Stage (n)'][:8], df['Total (T_n)'][:8], 
                marker='o', linewidth=3, markersize=8, color='red')
ax2.fill_between(df['Stage (n)'][:8], df['Total (T_n)'][:8], alpha=0.3, color='red')
ax2.set_title('$T_n = 1 + \\sum_{k=1}^{n-1} 6k$: Total Accumulated Hexagons', 
              fontsize=14, fontweight='bold')
ax2.set_xlabel('Stage (n)')
ax2.set_ylabel('Total Hexagons')
ax2.grid(True, alpha=0.3)

# Add value labels on points
for i in range(8):
    ax2.text(df['Stage (n)'][i], df['Total (T_n)'][i] + 2,
             f'{df["Total (T_n)"][i]}', ha='center', va='bottom', fontweight='bold')

plt.suptitle('🌊 SIGMA (Σ) AS ACCUMULATED GROWTH', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("\n📖 WHAT IS k IN THE SIGMA NOTATION?")
print("In the formula: T_n = 1 + Σ(k=1 to n-1) 6k")
print("• n = current stage we want to find total for")
print("• k = counter/index for previous rings we're adding up")
print("• k goes from 1 to (n-1) because we sum all previous rings")
print("• Each ring k contributes 6k hexagons to the total")

# Create a visual explanation of k
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Show the sigma expansion for n=5
n_example = 5
x_positions = np.arange(1, n_example)
y_positions = [6*k for k in x_positions]

bars = ax.bar(x_positions, y_positions, color=['lightcoral', 'lightblue', 'lightgreen', 'plum'][:len(x_positions)],
              edgecolor='black', linewidth=2, alpha=0.8)

ax.set_title(f'Breaking Down Σ for Stage {n_example}: $T_5 = 1 + \\sum_{{k=1}}^{{4}} 6k = 1 + 6(1) + 6(2) + 6(3) + 6(4)$', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('k (ring number from seed)')
ax.set_ylabel('Hexagons in ring k: 6k')
ax.set_xticks(x_positions)
ax.grid(True, alpha=0.3)

# Add annotations
for i, (x, y) in enumerate(zip(x_positions, y_positions)):
    ax.annotate(f'Ring k={int(x)}\nAdds 6×{int(x)}={int(y)}', 
                xy=(x, y/2), ha='center', va='center', 
                fontweight='bold', fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Add total calculation
total = 1 + sum(y_positions)
ax.text(0.02, 0.98, f'Total: T_5 = 1 + {" + ".join(map(str, y_positions))} = {total}', 
        transform=ax.transAxes, fontsize=12, fontweight='bold',
        verticalalignment='top', bbox=dict(boxstyle="round,pad=0.5", facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.show()

# =============================================================================
# SECTION 3: TRIANGLE TREE TESSELLATION 🌲
# =============================================================================

print("\n" + "="*60)
print("🌲 BONUS: Triangle Tree Tessellation")
print("="*60)

def triangle_tree_added(n):
    """Number of triangles added at stage n"""
    return 3 * (n - 1)

def triangle_tree_total(n):
    """Total triangles at stage n"""
    return 1 + 3 * (n - 1) * n // 2

# Create triangle data
triangle_stages = list(range(1, 11))
b_n_values = [triangle_tree_added(n) for n in triangle_stages]
B_n_values = [triangle_tree_total(n) for n in triangle_stages]

triangle_df = pd.DataFrame({
    'Stage': triangle_stages,
    'New Triangles (b_n)': b_n_values,
    'Total Triangles (B_n)': B_n_values
})

print("🧠 HIGH SCHOOL PROBLEM: Triangle Tree Tessellation")
print("Each stage adds triangular 'tree rings' around the central triangle.")
print("\nSequence: 1, 4, 10, 19, 31, 46, 64, 85, 109, 136...")
print(triangle_df.head(8))

# Visualize triangle growth
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# New triangles added
ax1.bar(triangle_df['Stage'][:8], triangle_df['New Triangles (b_n)'][:8], 
        color='forestgreen', alpha=0.7, edgecolor='black')
ax1.set_title('$b_n = 3(n-1)$: New Triangles Added', fontsize=14, fontweight='bold')
ax1.set_xlabel('Stage (n)')
ax1.set_ylabel('New Triangles Added')
ax1.grid(True, alpha=0.3)

# Total triangles
ax2.plot(triangle_df['Stage'][:8], triangle_df['Total Triangles (B_n)'][:8], 
         marker='s', linewidth=3, markersize=8, color='darkgreen')
ax2.fill_between(triangle_df['Stage'][:8], triangle_df['Total Triangles (B_n)'][:8], 
                 alpha=0.3, color='forestgreen')
ax2.set_title('$B_n = 1 + \\frac{3(n-1)n}{2}$: Total Triangles', fontsize=14, fontweight='bold')
ax2.set_xlabel('Stage (n)')
ax2.set_ylabel('Total Triangles')
ax2.grid(True, alpha=0.3)

plt.suptitle('🌲 TRIANGLE TREE TESSELLATION GROWTH', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print(f"\n📊 SOLUTION TO TRIANGLE PROBLEM:")
print(f"(a) b_n = 3(n-1) - triangles added at stage n")
print(f"(b) B_1 = 1, B_n = B_(n-1) + 3(n-1) - recursive formula")  
print(f"(c) B_n = 1 + 3(n-1)n/2 - explicit formula")
print(f"(d) At stage 10: B_10 = {triangle_tree_total(10)} triangles")

# =============================================================================
# HISTORICAL CONTEXT
# =============================================================================

print("\n" + "="*60)
print("🏛️ HISTORICAL MATHEMATICAL SYMBOLS")
print("="*60)
print("• Σ (Sigma): Greek letter meaning 'sum', introduced by Euler (1707-1783)")
print("• n subscripts: Modern notation developed in 19th century")
print("• Tessellations: Found in Islamic art (8th century), Greek mosaics")
print("• Arithmetic sequences: Known to ancient Babylonians (~2000 BCE)")
print("• Gauss's triangle numbers: Young Gauss (1777-1855) summed 1+2+...+100")

print("\n🎯 KEY TAKEAWAYS:")
print("• SEED (a_n): Represents growth increment at each stage")  
print("• SIGMA (Σ): Accumulates all previous growth")
print("• INDEX (k): Counts through each growth layer")
print("• STAGE (n): Current position in the sequence")

print("\n✨ Visual associations help understand abstract math!")
print("🌱 Seed → 🔢 Sequence → 📐 Geometry → 🧠 Understanding")
