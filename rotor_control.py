# Just importing Python's standard libraries
import sys
import time
# This is the navio's specific utilities
import navio.pwm
import navio.util

# Default min and max
SERVO_MIN = 1.18 #1.250 #ms
SERVO_MAX = 1.750 #ms

pwmArray = []

def calibrate():
    # TODO: Find max and min and save them
    return 0

def set_rotors(**kwargs):
    # Takes values from 0 to 1 where 0 is min spinning, 1 is max spinning, and -1 is stop
    def convert(val):
        if(val == -1): return 0
        return val * (SERVO_MAX - SERVO_MIN) + SERVO_MIN

    if('a' in kwargs): pwmArray[2].set_duty_cycle(convert(kwargs['a']))
    if('b' in kwargs): pwmArray[0].set_duty_cycle(convert(kwargs['b']))
    if('c' in kwargs): pwmArray[3].set_duty_cycle(convert(kwargs['c']))
    if('d' in kwargs): pwmArray[1].set_duty_cycle(convert(kwargs['d']))

def test_rotors():
    navio.util.check_apm()

    PWM_OUTPUT = 0
    # These are just some good values to know when seting the motor power


    # Now every time we want to use a motor, we have to enable it first
    # Let's enable all 4 (they're numbered 0-3)

    for num in range(0,3+1): # This loops over 0,1,2,3
    	pwm = navio.pwm.PWM(num)
    	pwm.set_period(50)
    	pwmArray.append(pwm)

    cycles = 1; # How many cycles you want to spin the rotors for
    # Otherwise it'll keep spinning forever

    while (cycles > 0):
    	cycles -= 1
    	# Now we alternate all motors between fast and slow
        for pwm in pwmArray:
            pwm.set_duty_cycle(SERVO_MIN)
            # They will keep spinning until we send a new signal
            time.sleep(.1)
            for pwm in pwmArray:
        		pwm.set_duty_cycle(SERVO_MIN)
            time.sleep(.1)

    # So even if you terminate the script, they will keep spinning
    # We have to send a stop signal to every motor before we leave
    for pwm in pwmArray:
        pwm.set_duty_cycle(0)
