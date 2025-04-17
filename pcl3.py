import matplotlib.pyplot as plt

# Sample data
lanes = ['Lane 1', 'Lane 2', 'Lane 3', 'Lane 4']
vehicle_counts = [10, 50, 80, 5]

plt.bar(lanes, vehicle_counts, color='skyblue')
plt.title("Real-Time Vehicle Count per Lane")
plt.xlabel("Lanes")
plt.ylabel("Vehicle Count")
plt.show()
