# Bloid
This is a custom, ball balancing robot. 

## CAD

<img width="644" height="506" alt="Screenshot 2025-07-14 at 4 35 45 AM" src="https://github.com/user-attachments/assets/2159ae69-98e9-4949-8ceb-7059062f93d1" />

## Software

<img width="287" height="379" alt="Screenshot 2025-07-14 at 4 37 16 AM" src="https://github.com/user-attachments/assets/a4b8bea8-8ad2-404d-b957-30863038bfd9" />

## Software setup

Depending on what device you are on and what directory you export to, the first few steps could vary, so in summary: **you need to ```cd``` into the ```/Software/Main``` folder**

From there, the setup process is very simple:

Create a new python virtual environment:

```
python -m venv env
```

Enter the environment:

```
source env/bin/activate
```

Install the required packages:

```
pip install opencv-python pigpio 
```

Start up the main program:

```
#Start up the pigpio daemon
sudo pigpiod
#Main code
python main.py
```

## Final Product

![1000004387](https://github.com/user-attachments/assets/3108bd6c-dd6b-4e91-bc90-f5ccc8102a9e)

![1000004389](https://github.com/user-attachments/assets/93c50e09-9985-4714-9c74-bc205221e27f)

![1000004386](https://github.com/user-attachments/assets/9fed8b3a-c16c-4109-bfb3-fc7ce4b3d050)

## BOM
|    Item    | Quantity | Vendor | Total Price |
| :-------- | :-------: | :----- | ----------: |
| Raspberry Pi | 1 | [PiShop USA](https://www.pishop.us/product/raspberry-pi-4-model-b-1gb/?srsltid=AfmBOorvizn3933kIKKK45gcBSmxiYC6vVZNzOPITzODrxT-XyKx8Tb-PpY) | $35.00 |
| Webcam |  1  |  [Walmart](https://www.walmart.com/ip/1080P-Web-Cam-HD-Camera-Webcam-with-Mic-Microphone-for-Computer-PC-Laptop-Notebook/7115471225?wmlspartner=wlpa&selectedSellerId=101287330&selectedOfferId=19192E1722E13AD9BEAA8E743E946E40&conditionGroupCode=1&gQT=1)| $7.99 |
| Servos Set | 1    | [Amazon](https://www.amazon.com/4-Pack-MG996R-Torque-Digital-Helicopter/dp/B07MFK266B?th=1) | $17.99 | 
| M3 Hardware (Set) | 1 | [Amazon](https://www.amazon.com/Taiss-540PCS-Stainless-Socket-Washers/dp/B0D4L6QRZB?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A2VILSBUHD1UD8&gQT=2&th=1) | $9.99 |
| Dupont Wires Set| 1 | [Amazon](https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78) | $6.98 |
| 3D Printer and filaments| Undef | Undef | Undef |

Net Total Cost (Not including 3D printer/filaments): $77.95
