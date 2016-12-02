import rotor_control as rc
import sensors
import time
import navio.util

#initialize this once
navio.util.check_apm()

rc.test_rotors()

# rc.set_rotors()
# time.sleep(2)
# rc.set_rotors(a=-1,b=-1,c=-1,d=-1)
#

sensors.init()

while(1!=0):
    time.sleep(0.2)
    sensors.get_data()
