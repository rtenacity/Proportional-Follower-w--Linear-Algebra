#!/usr/bin/python
# coding: utf-8

from time import sleep
import sys
from ev3dev.auto import *

left_motor = LargeMotor(OUTPUT_B);  assert left_motor.connected
right_motor = LargeMotor(OUTPUT_C); assert right_motor.connected
ts = TouchSensor();    	assert ts.connected
col= ColorSensor(); 	assert col.connected
col.mode = 'COL-REFLECT'

kp = 1
power = 15
target = 55

lcorrection = 0
rcorrection = 0

left_motor.run_direct()
right_motor.run_direct()

while True:
    if ts.value():
        break
    refRead = col.value()
    error = target - refRead
    if error > 0:
        lcorrection = kp * error
    elif error < 0:
        rcorrection = -kp * error
    if (lcorrection+power) >= 100:
        lcorrection = 100-power
    if (rcorrection+power) >= 100:
        rcorrection = 100-power
    
    print(str(target)+","+str(refRead)+","+str(error)+","+str(lcorrection+power)+ ","+str(rcorrection+power))
    left_motor.duty_cycle_sp= int(power + lcorrection)
    right_motor.duty_cycle_sp= int(power + rcorrection)
    sleep(0.01)
left_motor.stop()
right_motor.stop()