

El servo-motor deberia estar alimentado con una fuente de alimentación externa de 5v y al menos 1A.

Para realizar esta receta lo limentaremos con la RPI con la salida de 3.3V, al no disponer de suficiente voltaje el funcionamiento no sera el optimo. 


```python
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 100)

print "Init program"


try:
    while True:
        print "Init bucle"
        print "5"
        p.start(5)
        time.sleep(2)
        p.stop()
        time.sleep(2)
        print "40"
        p.start(40)
        time.sleep(2)
        p.stop()
        time.sleep(2)
        print "70"
        p.start(70)
        time.sleep(5)
        p.stop(2)
        


except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    
```
    
    
    
