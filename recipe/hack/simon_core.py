#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LED_RED = 21
LED_GREEN = 20

BUTTON_RED = 17
BUTTON_GREEN = 4

BUZZ = 22
SECS_BLINK = 2
SECS_USER = 1.5
import random

def myrand():
    val=random.random()
    return val


def setup_in(button):
    GPIO.setup(button,GPIO.IN)

def setup_out(led):
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)

def blink(led):
    print(str(led) + " on")
    GPIO.output(led, GPIO.HIGH)
    time.sleep(SECS_BLINK)
    print(str(led) + " off")
    GPIO.output(led, GPIO.LOW)
    time.sleep(SECS_BLINK)


def mybuzz(buzz):
    GPIO.output(buzz, True)
    time.sleep(2)
    GPIO.output(buzz, False)
    time.sleep(2)


def buzz():
    print "BUUUUZZ"
    #blink(BUZZ)
    mybuzz(BUZZ)

if __name__  == "__main__":
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    setup_out(LED_RED)
    setup_out(LED_GREEN)
    setup_in(BUTTON_RED)
    setup_in(BUTTON_GREEN)
    setup_out(BUZZ)


    try:
        while False:
            blink(LED_RED)
            if GPIO.input(BUTTON_RED) == False:
	        print "button ok"
                break	
        while True:
            val = myrand()
            if (val<0.5):
                blink(LED_RED)
                if GPIO.input(BUTTON_RED) == True or GPIO.input(BUTTON_GREEN) == False:
                    break
                else:
                    print "OK RED"
            else:
                blink(LED_GREEN)
                if GPIO.input(BUTTON_GREEN) == True or GPIO.input(BUTTON_RED) == False:
                    break
                else:
                    print "OK GREEN"
            #print "Blink led"
            #blink(LED)
            SECS_BLINK = SECS_BLINK*0.9
            print "LEVEL %f"%SECS_BLINK
    except KeyboardInterrupt:
        print "Exception"
    buzz()
    GPIO.cleanup()
