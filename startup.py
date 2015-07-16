#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import threading

pins = [18, 23]

def main():
    init()
    
def init():
    print '[*] Initiate LEDs [*]'
    
    for pin in pins:
            GPIO.output(pin, True)
            time.sleep(0.1)
            GPIO.output(pin, False)
    
    print '[*] Process Complete [*]'
    
def initWireless():

def activeWireless():

def errorWireless():

def errorWiFi():

if __name__ == '__main__':
    main()