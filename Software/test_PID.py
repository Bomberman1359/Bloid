import time
from use_test_PID import PID  # assuming your code is saved in pid.py

pid = PID(gains=[2.0, 0.1, 0.05], scale_factor=1.0, filter_coeff=0.8)

target = [0.0, 0.0]  # center of the platform
test_positions = [
    [0.0, 0.0],       # Start centered
    [0.04, 0.02],     # Sudden displacement
    [0.04, 0.02],     # Hold
    [0.0, 0.0]        # Return
]


for pos in test_positions:
    theta, phi = pid.compute(target, pos)
    print(f"Current: {pos}, θ = {theta:.2f}°, φ = {phi:.4f}")
    time.sleep(0.1)
