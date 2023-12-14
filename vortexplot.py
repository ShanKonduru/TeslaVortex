import matplotlib.pyplot as plt
import numpy as np

def vortex_math(number, multiplier, modulus):
    result = number * multiplier % modulus

    # Reduce the result to a single-digit root
    while result > 9:
        result = sum(map(int, str(result)))

    return result

# Example usage:
number_input = 100 # int(input("Enter a number: "))
multiplier_input = 7 # int(input("Enter the multiplier: "))
modulus_input = 27 #  int(input("Enter the modulus: "))
num_iterations = 10000 # int(input("Enter the number of iterations: "))

# Generate vortex math results
results = []
for _ in range(num_iterations):
    result = vortex_math(number_input, multiplier_input, modulus_input)
    results.append(result)

# Plotting the results in a polar plot
theta = np.linspace(0, 2 * np.pi, num_iterations, endpoint=False)
colors = plt.cm.viridis(np.linspace(0, 1, num_iterations))[:, :3]  # Extract RGB values

# Convert RGB to hexadecimal format
hex_colors = ['#%02x%02x%02x' % tuple(int(255 * x) for x in color) for color in colors]

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, results, marker='o', linestyle='-', color=hex_colors)

ax.set_title('3-6-9 Vortex Math Results')
ax.set_xticks(theta)
ax.set_xticklabels(range(1, num_iterations + 1))
ax.set_yticks(range(10))
ax.set_yticklabels(range(10))

plt.show()