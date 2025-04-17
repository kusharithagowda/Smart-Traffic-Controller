import numpy as np
import matplotlib.pyplot as plt

# Example accuracies over iterations (simulated)
iterations = np.arange(1, 11)
accuracies = np.array([0.85, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.92, 0.93, 0.94]) * 100

plt.plot(iterations, accuracies, marker='o')
plt.title("Model Accuracy Over Time")
plt.xlabel("Iteration")
plt.ylabel("Accuracy (%)")
plt.grid()
plt.show()
