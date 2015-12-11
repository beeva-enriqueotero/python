#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LED_RED = 21
LED_GREEN = 20

BUTTON_RED = 17
BUTTON_GREEN = 4

BUZZ = 22
SECS_BLINK = 2
SECS_USER = 2
import random

def myrand():
    val=random.random()
    return val


def setup_in(button):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button,GPIO.IN)

def setup_out(led):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)

def blink(led):
    print(str(led) + " on")
    GPIO.output(led, GPIO.HIGH)
    time.sleep(SECS_BLINK)
    print(str(led) + " off")
    GPIO.output(led, GPIO.LOW)
    time.sleep(SECS_BLINK)


def buzz():
    print "BUUUUZZ"

if __name__  == "__main__":
    GPIO.cleanup()

    setup_out(LED_RED)
    setup_out(LED_GREEN)
    setup_in(BUTTON_RED)
    setup_in(BUTTON_GREEN)


    try:
        while True:
            blink(LED_RED)
            if GPIO.input(BUTTON_RED) == False:
	        print "button ok"
                break	
        while False:
            val = myrand()
            if (val<0.5):
                blink(LED_RED)
                if GPIO.input(BUTTON_RED) == True:
                    break
                else:
                    print "OK RED"
            else:
                blink(LED_GREEN)
                if GPIO.input(BUTTON_GREEN) == True:
                    break
                else:
                    print "OK GREEN"
            #print "Blink led"
            #blink(LED)
    except KeyboardInterrupt:
        print "Exception"
    buzz()
    GPIO.cleanup()
