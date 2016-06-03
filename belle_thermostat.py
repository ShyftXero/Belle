#!/usr/bin/env python3
#20160520 - shyft
#belle_temp.py
#use this to turn the thermostat on and off
import time
import redis
import random

onPi = False

if onPi:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)


#possible api
#/api/<zone>/   returns current vals
# /api/<zone>/mode/<"heat"|"cool"|"off">
# /api/<zone>/temp/<target_temp>
# /api/<zone>/fan/
# /api/<zone>/fan/<"on"|"off">


stock_names=["cat", "dog", 'wolf','cow']

class Zone:
    """defines a Zone in the facility
    establishes a few default parameters and
    """

    def __init__(self, name, targetTemperature=72, AC_pin=1, Fan_pin=2, Heater_pin=3, modes=['COOL', 'HEAT', 'OFF']):
        self.name = name
        self.targetTemperature = targetTemperature
        self.current_temp = targetTemperature
        self.AC_pin = AC_pin
        self.Fan_pin = Fan_pin
        self.Heater_pin = Heater_pin
        self.minTemp = 60
        self.maxTemp = 90
        self.current_mode = "off"  #unit modes "cool", "heat", "off"
        self.fudge = 3  # how much the readings could be off by
        self.modes = modes

    def validMode(self, option):
        if option.upper()  in self.modes:
            return True
        else:
            return False

    def validTemp(self, option):
        if int(option) >= self.minTemp and int(option) <= self.maxTemp:
            return True
        else:
            return False

    def setMode(self, mode):
        if self.validMode(mode):
            self.current_mode = mode
            return "ok - unit mode " + self.current_mode
        return "invalid mode"

    def getTemp(self, zone):
        return self.current_temp

    def setTemp(self, temp):
        if self.validTemp(temp):
            self.targetTemperature = int(temp)
            return "ok - temp %s " % self.targetTemperature
        return "invalid temp"

    def fanOn():
        if onPi:
            GPIO.output(self.Fan_pin, 1)
        return "ok - fan on"

    def fanOff():
        if onPi:
            GPIO.output(self.Fan_pin, 0)
        return "ok - fan off"

    def setFudge(self, fudge):
        self.fudge = fudge
        return "ok - fudge " + self.fudge

    def getFudge():
        return self.fudge


    def getPins():
        return "AC_pin %d, Fan_pin %d, Heater_pin %d" % (self.AC_pin, self.Fan_pin, self.Heater_pin)


#
#
# upstairs = BelleZone(name="Upstairs", AC_pin=1, Fan_pin=2, Heater_pin=3) #this
# downstairs = BelleZone(name="Downstairs", AC_pin=1, Fan_pin=2, Heater_pin=3)
#
# downstairs.setTemp(30)
# print(upstairs.targetTemperature)
#
#
# while True:
#         print("upstairs is " + upstairs.getTemp())
#         print("downstairs is " + downstairs.getTemp())
#         time.sleep(2)
