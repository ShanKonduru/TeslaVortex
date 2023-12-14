import matplotlib.pyplot as plt
import numpy as np

def plot_circle_with_dots(diameter=50, num_dots=9):
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

    # Set aspect ratio to be equal, and adjust plot limits
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([-radius, radius])
    ax.set_ylim([-radius, radius])

    # Add title
    ax.set_title('Circle with Dots on Perimeter')

    plt.show()

# Example usage with default values
plot_circle_with_dots()
