#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

pins = [18, 23]

def main():
    init()
    time.sleep(0.5)
    print str(initWireless())
    
def init():
    print '[*] Initiate LEDs [*]'
    
    for pin in pins:
            GPIO.output(pin, True)
            time.sleep(0.1)
            GPIO.output(pin, False)
    
    print '[*] Process Complete [*]'
    
def initWireless():
    print '[*] Checking for Wireless Card [*]'
    
    os.system('iwconfig > iwconfig.txt')
    
    if int(os.path.getsize('iwconfig.txt')) > 0:
        file = open('iwconfig.txt', 'r')
        for line in file.readlines():
            if 'wlan' in line:
                print '[*] Wireless Card Detected [*]'
                file.close()
                return True
                activeWireless()
            else:
                print '[!] No Wireless Card Detected [!]'
                file.close()
                return False
                errorWireless()
            break
    else:
        print '[!] No Wireless Card Detected [!]'
        return False
        errorWireless()

def activeWireless():
    delete('iwconfig.txt')
    
    GPIO.output(pins[0], True)

def errorWireless():
    while True:
        GPIO.output(pins[0], True)
        time.sleep(0.5)
        GPIO.output(pins[0], False)
        time.sleep(0.5)
    
    delete('iwconfig.txt')
    print 'dsfsfd'


def delete(c):
    os.system('rm ' + c)

if __name__ == '__main__':
    main()