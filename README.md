# 🎲 Galton Board Simulation

This project implements a **Galton Board simulation** using Python.  
The **Galton Board**, invented by Sir Francis Galton, demonstrates how **random binary decisions** (left/right) can produce an **approximately normal distribution**, resembling the well-known **bell curve**.

---

## 📌 Project Description

In this simulation:

- 🔵 **3,000 marbles** are dropped.
- 🟡 Each marble goes through **12 levels of pegs**.
- 🔴 At the end, marbles fall into **13 possible containers** (from 0 to 12), depending on how many times they went right.
- 📊 A **graphical histogram** is generated using `matplotlib` to visualize the final distribution.

---

## ⚙️ How the Program Works

### 🧩 Code Structure

The code is organized into two main functions:

- `simulate_marbles(num_marbles, levels)`  
  Simulates each marble’s path and tracks how many marbles fall into each container based on the number of right moves.

- `plot_histogram(data, levels)`  
  Plots a bar chart representing the number of marbles per container using the `matplotlib` library.

### 🧪 Libraries Used

- `random`: To simulate each marble's binary decision (left or right) at each level.
- `matplotlib.pyplot`: To display the final histogram clearly and visually.

> Note: The simulation **does not use** the `normal()` function. The normal-like distribution emerges naturally from repeated binary decisions.

---

## ▶️ How to Run

### 📌 Requirements

Install the required library using pip:

```bash
pip install matplotlib
