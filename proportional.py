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

kp = 1 #do not set kp as a decimal/float
power = 30
target = 55

lcorrection = 0
rcorrection = 0

def nudge_left(val):
    left_motor.duty_cycle_sp(int(val))
def nudge_right(val):
    right_motor.duty_cycle_sp(int(val))

left_motor.run_direct()
right_motor.run_direct()


while True:
    if ts.value():
        break
    refRead = col.value()
    error = target - refRead
    if error > 0:
        lcorrection = int(kp * error)
    elif error < 0:
        rcorrection = int(-kp * error)

    left_motor.duty_cycle_sp= power + lcorrection
    right_motor.duty_cycle_sp= power + rcorrection
    sleep(0.01)
left_motor.stop()
right_motor.stop()