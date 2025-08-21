import random
import matplotlib.pyplot as plt

# Total number of random points
num_points = 10000

inside_circle = 0
x_inside = []
y_inside = []
x_outside = []
y_outside = []

for _ in range(num_points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if x**2 + y**2 <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# Estimate of Pi
pi_estimate = 4 * inside_circle / num_points
print(f"Estimated Pi: {pi_estimate}")

# Plot the simulation
plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
plt.title("Monte Carlo Simulation for Estimating Pi")
plt.legend()
plt.axis("equal")
plt.show()
