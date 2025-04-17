import matplotlib.pyplot as plt
import numpy as np

# Example traffic density values
traffic_density = np.linspace(0, 1, 10)  # density from 0 to 1 (normalized)

# Example calculation of green light duration
base_time = 30
alpha = 50
green_light_duration = base_time + alpha * traffic_density

# Plotting the graph
plt.plot(traffic_density, green_light_duration, marker='o')
plt.title("Traffic Density vs. Green Light Duration")
plt.xlabel("Traffic Density (vehicles per meter)")
plt.ylabel("Green Light Duration (seconds)")
plt.grid()
plt.show()
