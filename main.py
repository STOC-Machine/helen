import rotor_control as rc
import time

rc.test_rotors()

rc.set_rotors()
time.sleep(2)
rc.set_rotors(a=-1,b=-1,c=-1,d=-1)
