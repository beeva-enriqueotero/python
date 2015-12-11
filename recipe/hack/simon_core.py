#!/usr/bin/env python

import time

LED_RED = 1
LED_GREEN = 2

BUTTON_RED = 11
BUTTON_GREEN = 12

BUZZ = 20
SECS_BLINK = 2
SECS_USER = 2
import random

def myrand():
    val=random.random()
    return val



def setup(led):

#    GPIO.cleanup()
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(led, GPIO.OUT)
    print setup

def blink(led):

    print(str(led) + " on")
#    GPIO.output(led, GPIO.HIGH)
    time.sleep(SECS_BLINK)
    print(str(led) + " off")
#    GPIO.output(led, GPIO.LOW)
    time.sleep(SECS_BLINK)


def buzz():
    print "BUUUUZZ"

if __name__  == "__main__":


    #setup(LED)

    try:
        while True:
            val = myrand()
            if (val<0.5):
                print BUTTON_RED
                blink(LED_RED)
                if GPIO.input(BUTTON_RED) == False:
                    break
                else:
                    print "OK"
            else:
                print BUTTON_RED
                blink(LED_RED)
                if GPIO.input(BUTTON_RED) == False:
                    break
                else:
                    print "OK"
            #print "Blink led"
            #blink(LED)
    except KeyboardInterrupt:
        print "Exception"
        GPIO.cleanup()
    buzz()
