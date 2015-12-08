## Push button recipe


![alt tag](../../static/button_circuit_mini.jpg)

Push button

![alt tag](../../static/push_button_colors_mini.jpg)


Circuit

![alt tag](../../static/push_button.jpg)



```python
#!/usr/bin/python


import RPi.GPIO as GPIO
import time as time

BUTTON_PIN = 11


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN,GPIO.IN)


while True:

    time.sleep(0.2)

    if GPIO.input(BUTTON_PIN) == False:
        print "Push button ok"

```
