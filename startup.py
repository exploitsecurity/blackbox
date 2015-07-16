#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

pins = [18, 23]

buttons = [24]

def main():
    init()
    time.sleep(0.5)
    if initWireless() == True:
        activeWireless()
        
        global t
        t = threading.Thread(target=initServer)
        t.start()
    else:
        errorWireless()
    
    initButton()
    
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
            else:
                print '[!] No Wireless Card Detected [!]'
                file.close()
                return False
            break
    else:
        print '[!] No Wireless Card Detected [!]'
        return False

def activeWireless():
    print '[*] Wireless Active in Mono Mode [*]'
    
    delete('iwconfig.txt')
    
    GPIO.output(pins[0], True)

def errorWireless():
    print '[!] Wireless Error unable to connect [!]'
    
    while True:
        GPIO.output(pins[0], True)
        time.sleep(0.5)
        GPIO.output(pins[0], False)
        time.sleep(0.5)
    
    delete('iwconfig.txt')
    print 'dsfsfd'

def initServer():
    print '[*] Starting WiFi Airspace Survey [*]'
    

    activeServer()
    os.system('kismet_server -c wlan0 > /dev/null &')
    
def activeServer():
    print '[*] WiFi Server is up and active [*]'
    GPIO.output(pins[1], True)
    print os.system('ps')
    
def errorServer():
    print '[!] Unable to connect to WiFi Server [!]'
    
def initButton():
    status = True
    delay = 0
    
    while status:
        if GPIO.input(buttons[0]) == False:
            delay += 1
            buttonDelay(delay)
            time.sleep(1)
        elif delay == 3:
            status = False
            reboot()
    
def buttonDelay(i):
    GPIO.output(pins[1], False)
    time.sleep(0.5)
    GPIO.output(pins[1], True)
    time.sleep(0.5)
    
def reboot():
    status = True
    counter = 0
    
    while status:
        if counter < 5:
            GPIO.output(pins[1], False)
            time.sleep(0.25)
            GPIO.output(pins[1], True)
            time.sleep(0.25)
            counter += 1
        else:
            status = False
            clearLEDS()
            os.system('sudo reboot')

def clearLEDS():
    for pin in pins:
        GPIO.output(pin, False)

def delete(c):
    os.system('rm ' + c)

if __name__ == '__main__':
    main()
    
    # kismet_server -c wlan0 > /dev/null &