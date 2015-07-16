#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import threading

pins = [18, 23]

def main():
    init()
    initWireless()
    
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
    
    if int(os.path.getsize('iwconfig')) > 0:
        file = open('iwconfig.txt', 'r')
        for line in file.readlines():
            if 'wlan' in line:
                print '[*] Wireless Card Detected [*]'
                file.close()
                activeWireless()
            else:
                print '[!] No Wireless Card Detected [!]'
                file.close()
                errorWireless()
            break
    else:
        print '[!] No Wireless Card Detected [!]'
        file.close()
        errorWireless()

def activeWireless():
    delete('iwconfig.txt')
    print 'hsudsj'

def errorWireless():
    delete('iwconfig.txt')
    print 'dsfsfd'


def delete(c):
    os.system('rm ' + c)

if __name__ == '__main__':
    main()