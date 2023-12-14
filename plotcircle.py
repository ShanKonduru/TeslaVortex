import matplotlib.pyplot as plt
import numpy as np
import random

def plot_circle_with_dots_and_lines(diameter=50, num_dots=9):
    radius = diameter / 2
    theta = np.linspace(0, 2 * np.pi, num_dots, endpoint=False)

    # Calculate coordinates of dots on the perimeter
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plot the circle
    circle = plt.Circle((0, 0), radius, edgecolor='b', facecolor='none')
    fig, ax = plt.subplots()
    ax.add_patch(circle)

    # Plot dots on the perimeter with associated numbers
    for i, (dot_x, dot_y) in enumerate(zip(x, y), start=1):
        ax.plot(dot_x, dot_y, marker='o', markersize=8, label=str(i))
        ax.text(dot_x, dot_y, str(i), ha='center', va='center', fontsize=10, fontweight='bold')

    # Lines connecting specific dots with random colors
    pairs = [(1, 2), (7, 8), (3, 9), (9, 6), (3, 6), (1, 5), (2, 4), (7, 5), (8, 4)]
    for pair in pairs:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generate random hex color
        line = plt.Line2D([x[pair[0] - 1], x[pair[1] - 1]], [y[pair[0] - 1], y[pair[1] - 1]],
                          color=color, linestyle='-', linewidth=1)
        ax.add_line(line)

    # Set aspect ratio to be equal, and adjust plot limits
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([-radius, radius])
    ax.set_ylim([-radius, radius])

    # Add title
    ax.set_title('Circle with Dots and Connecting Lines')

    plt.show()

# Example usage with default values
plot_circle_with_dots_and_lines()
