import csv
import matplotlib.pyplot as plt

timestamps = []
x_vals = []
y_vals = []
theta_vals = []
phi_vals = []

# Load the CSV file
with open("pid_log.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        timestamps.append(float(row["Timestamp"]))
        x_vals.append(float(row["X"]))
        y_vals.append(float(row["Y"]))
        theta_vals.append(float(row["Theta (deg)"]))
        phi_vals.append(float(row["Phi"]))

# Normalize time (start from 0)
start_time = timestamps[0]
timestamps = [t - start_time for t in timestamps]

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(timestamps, theta_vals, label='Theta (°)', color='blue')
plt.ylabel("Theta (deg)")
plt.title("PID Output Over Time")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(timestamps, phi_vals, label='Phi', color='green')
plt.ylabel("Phi (magnitude)")
plt.xlabel("Time (s)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
