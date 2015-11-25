## RGB led recipe

```python
#!/usr/bin/env python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()

PIN_RED=0
PIN_GREEN=2
PIN_BLUE=1

wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)

wiringpi.digitalWrite(PIN_RED, 0)
wiringpi.digitalWrite(PIN_GREEN, 0)
wiringpi.digitalWrite(PIN_BLUE, 0)
```
