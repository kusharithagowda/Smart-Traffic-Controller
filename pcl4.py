import matplotlib.pyplot as plt

weather_conditions = ['Clear', 'Rain', 'Snow']
adjusted_durations = [30, 36, 42]  # Hypothetical green light durations

plt.bar(weather_conditions, adjusted_durations, color=['green', 'blue', 'gray'])
plt.title("Impact of Weather on Green Light Duration")
plt.xlabel("Weather Conditions")
plt.ylabel("Adjusted Green Light Duration (seconds)")
plt.show()
