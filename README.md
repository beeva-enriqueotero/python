# RPI GPIO 


Table of contents
=================

* [Python Recipes](#python-recipes)
* [Protoboard internal connections](#protoboard-internal-connections)
* [Access to RPI from laptop](#access-to-rpi-from-laptop)
* [GPIO pinout](#gpio-pinout)



Python Recipes
--------------

![alt tag](static/raspberry-pi-python-1-mini.jpg)

* [Led](recipe/led/README.md)
* [Led RGB](recipe/rgb_led/README.MD)
* [Push button](recipe/push_button/README.md)
* [Buzzer](recipe/buzzer/README.md)
* [Sensor Temperature](recipe/sensor_temperature/README.md)
* [Sensor Light](recipe/sensor_light/README.md)
* [Mini placas de Leds](recipe/mini_placas_leds)

Protoboard
-------------------------------

Internal connections
![alt tag](static/conexiones_protoboard2_mini.jpg)

Wires 
![alt tag](static/cables.jpg)

Connections
![alt tag](static/protoboard_cables.jpg)


Access to RPI from laptop
-------------------------


UART port in RPI

![alt tag](static/mini-uart.jpg)

Example module connection

![alt tag](static/uart_laptop_rpi_mini2_mini.jpg)


| RPI   |      Module      |
|----------|:-------------:|
| VCC | + 5V |
| Tx | GPIO 14 (UART TXD) |
| Rx | GPIO 15 (UART RXD) |
| Gnd | GND |


```bash
sudo apt-ger install ckermit # Install ckermit program (for serial port)
sudo reboot
sudo kermit -l /dev/ttyAMA0 # (or /dev/ttyAMA1)

# Configuration
C-Kermit> set speed 115200
C-Kermit> set parity none
C-Kermit> set flow-control none
C-Kermit> set carrier-watch off
C-Kermit> connect

Connecting to /dev/ttyAMA0, speed 115200
 Escape character: Ctrl-\ (ASCII 28, FS): enabled
Type the escape character followed by C to get back,
or followed by ? to see other options.
----------------------------------------------------
# Click enter

Raspbian GNU/Linux 7 raspberrypi ttyAMA0

raspberrypi login: pi
Password:

pi@raspberrypi:~$ 

```

GPIO pinout
-----------

![alt tag](static/Raspberry-Pi-GPIO-pinouts.png)






