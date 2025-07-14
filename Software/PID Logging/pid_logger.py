import time
import csv
from use_test_PID import PID  # Make sure this filename is correct

# Initialize PID with your chosen gains
pid = PID(gains=[2.0, 0.1, 0.05], scale_factor=1.0, filter_coeff=0.8)

target = [0.0, 0.0]  # Ball should stay centered
log_data = []

# Simulated test positions (change as needed)
test_positions = [
    [0.04, 0.02],   # Step input
    [0.04, 0.02],
    [0.03, 0.015],
    [0.02, 0.01],
    [0.01, 0.005],
    [0.00, 0.00],   # Returns to center
]

# Collect data for each test point
for i, pos in enumerate(test_positions):
    theta, phi = pid.compute(target, pos)
    log_data.append([time.time(), pos[0], pos[1], theta, phi])
    print(f"{i}: pos={pos}, θ={theta:.2f}°, φ={phi:.4f}")
    time.sleep(0.1)  # Simulate control loop delay

# Write to CSV
with open("pid_log.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Timestamp", "X", "Y", "Theta (deg)", "Phi"])
    writer.writerows(log_data)

print("✅ PID data logged to 'pid_log.csv'")
