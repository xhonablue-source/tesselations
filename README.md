# 🌱 MathCraft: Seed Tessellation & Sequences

A visual and interactive Streamlit app for high school students exploring sequences through geometric tessellations. Students discover how patterns emerge from a single seed, building both visual intuition and algebraic understanding.

---

## 🚀 Live App

[mathcraft-tesselations.streamlit.app](https://mathcraft-tesselations.streamlit.app)

---

## 📚 What It Teaches

### 🔷 Section 1: Visualizing $a_n$ as a Growth Seed
- Explains the hexagonal tessellation from a single center (seed).
- Shows how each stage adds a ring of hexagons.
- Demonstrates the formula:  
  \[
  a_n = 6(n - 1)
  \]

### 🔢 Section 2: Understanding Sigma $\\Sigma$
- Teaches how summation builds total counts:
  \[
  T_n = 1 + \\sum_{k=1}^{n-1} 6k = 1 + 3n(n - 1)
  \]
- Students see how $k$ indexes the ring layers.

### 🌲 Section 3: Triangle Tree Tessellation
- Extends to triangle-based tessellations:
  \[
  B_n = 1 + 3 \\cdot \\frac{(n-1)n}{2}
  \]
- Encourages comparison between hexagonal and triangular patterns.

---

## 📂 File Structure

