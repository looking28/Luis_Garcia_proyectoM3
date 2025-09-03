# Luis_Garcia_proyectoM3.py
# Physical Simulation of a Galton Board
# Author: Luis Alfonso Garcia Siguenza
# Date: 2025-09-02
# Description: This program simulates a Galton Board with 3,000 marbles and 12 levels.

import random
import matplotlib.pyplot as plt

#Simulate the marbles

def simulate_marbles(num_marbles=3000, levels=12):
    """
    Simulates the fall of marbles through a Galton board.

    Args:
        num_marbles (int): Number of marbles to simulate.
        levels (int): Number of levels (obstacles) in the board.

    Returns:
        list: List with the number of marbles in each container.
    """
    # List to count marbles per container (from 0 to levels)
    containers = [0] * (levels + 1)

    # Simulate each marble
    for _ in range(num_marbles):
        right_moves = 0  # Counts how many times the marble goes right

        for _ in range(levels):
            
            # Randomly choose: right if < 0.5, left if ≥ 0.5
            if random.random() < 0.5:
                right_moves += 1  # Goes to the right

        # The final container is determined by the number of right moves
        containers[right_moves] += 1

    return containers


#Plot histogram

def plot_histogram(data, levels=12):
    """
    Plots a histogram showing the number of marbles in each container.

    Args:
        data (list): List with the number of marbles per container.
        levels (int): Number of levels in the Galton board.
    """
    # Container labels: from 0 to levels
    containers = list(range(levels + 1))

    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.bar(containers, data, color='skyblue', edgecolor='black')

    # Title and axis labels
    plt.title('Distribution of Marbles in the Galton Board')
    plt.xlabel('Container (Number of times marble went right)')
    plt.ylabel('Number of Marbles')
    plt.xticks(containers)

    # Display the plot
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Simulate the Galton board
    results = simulate_marbles(num_marbles=3000, levels=12)

    # Plot the histogram
    plot_histogram(results, levels=12)