---
Title: "Bloid"
Author: "Chunhwee Choi, Yash Sethuramen, Jackson"
Description: "A ball balancing machine"
Created_at: "2025-07-11"
---
# Design Journal
Total Number of Hours Spent: 72 Hours

## Brainstorming and material gathering: 7/11/2025-7/12/2025, 8 Hours
We had absolutely no idea what to create. We thought there would be a theme but it turned out there wasn't. It took us a while to come up with an idea, but in the end we decided to go with a ball balancing machine, which Yash and Jack remembered watching from past videos.
With an idea, we started collecting materials that we thought were necessary for the project. We first started with the huge servos, which we started with 6 of them for a 6 armed robot. 
We also gathered a bunch of wires and used Yash's raspberry pi to wire things together with a breadboard.

## CAD, Software, and Hardware: 7/12/2025 - 7/14/2025, 64 Hours
We decided to split roles. Jack would work on the CAD while Chunhwee would work on the main coding and software. Yash would do any other tasks or assist when necessary. 

### Tracking:
We decided to use a ball tracking algorithm that Yash has developed beforehand. We figured that we had to use a camera that would be mounted on a camera holder that looks at the ball from the top.
While it would have been ideal to put the camera at the bottom, we had no access to clear platforms for the camera to see through.
The way the ball tracker works is that we first take photos of the ball, remove it's background, feed it into a HSV algorithm and input the minimum and maximum HSV values into the tracking algorithm so that the camera would track that specific colored ball.

![Photo on 7-13-25 at 9 09 PM #2](https://github.com/user-attachments/assets/80747b60-e4c2-4fdb-9f02-c6a2d9525ec7)

![Photo on 7-13-25 at 6 09 PM](https://github.com/user-attachments/assets/fa0e95cb-dc11-4aee-88f5-4175dc3cae61)

We had to experiment with many different types of balls since the webcam quality wasn't the best, and we had a lot of trouble tracking. In the end we decided to 3D-print a red ball, and while the tracking wasn't perfect, with a white platform in the background, the tracking would have worked out.
The tracking software would send the (x,y,z) coordinates of the ball, which would be sent to the reverse kinematics code.

### Reverse Kinematics and PID:
To actually figure out how the platform should be balanced based on the ball's position, we had to figure out the math for reverse kinematics. While 2D reverse kinematics was doable, 3D was a whole another story.
In the end, we vibe coded the formula and used test values and forward kinematics to confirm the accuracy of the math.

<img width="519" height="289" alt="Screenshot 2025-07-14 at 3 05 01 AM" src="https://github.com/user-attachments/assets/713fb997-47fc-4708-bf71-a3b1000d1335" />

For the PID, we also vibe coded. We came up with different methods to test the accuracy of the PID as well, such as creating a table of sample values to see whether the platform would move smoothly.
This will lead to actually moving the servos.

<img width="673" height="423" alt="Screenshot 2025-07-14 at 3 05 37 AM" src="https://github.com/user-attachments/assets/d46d36e3-f247-4dae-a899-1648a4de9be8" />

### CAD
Cadding the whole hardware was the most difficult part, as we had to calculate/set all the lengths and values accurately for the math in the Reverse kinematics and PID to actually work.
(Jack talk about ur experiences)
<img width="552" height="483" alt="Screenshot 2025-07-14 at 3 58 52 AM" src="https://github.com/user-attachments/assets/6d4643be-b018-48a1-952f-4c5e7154806b" />

<img width="423" height="375" alt="Screenshot 2025-07-14 at 2 55 12 AM" src="https://github.com/user-attachments/assets/810c78ef-9a29-460d-8096-df0c92f06335" />

(add final images)

### Hardware
Building the hardware was the greatest strugle. The main issue was the ball mates, which took many different 3D printing attempts to pull of, since the PLA was so weak and the parts kept on breaking.
For the camera mount, we ended up cutting up cardboard and created pillars, where the camera would be able to mount.
(edit later)

All of these steps we worked on at the same time gradually during the listed time periods.


