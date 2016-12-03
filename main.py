import rotor_control as rc
import math
import sensors
import time
import navio.util

#initialize this once
navio.util.check_apm()

rc.test_rotors()

rc.set_rotors()
time.sleep(2)
rc.set_rotors(a=-1,b=-1,c=-1,d=-1)

sensors.init()

class PID:

    HOVER_SPEED = 0.25

    def __init__(self, P=2.0, I=0.0, D=1.0, Derivator=0, Integrator=0, Integrator_max=500, Integrator_min=500):
        
        self.speed_a = self.HOVER_SPEED
        self.speed_b = self.HOVER_SPEED
        self.speed_c = self.HOVER_SPEED
        self.speed_d = self.HOVER_SPEED

        self.start = True
        self.pitch_init = 0.0
        self.roll_init = 0.0

        self.P = P
        self.I = I
        self.D = D
        self.Derivator = Derivator
        self.Integrator = Integrator
        self.Integrator_max = Integrator_max
        self.Integrator_min = Integrator_min

        self.pitch = 0.0 # Axis 0
        self.roll  = 0.0 # Axis 1
        self.yaw  =  0.0 # Axis 2

        self.p_tune = 556009.591334/750000.0
 
        self.set_point = 0.0 # Ideal state for now is hover
        self.error=0.0
        self.P_correction = 0.0

        self.iterations = 0

    def update(self, val, axis=0):

        # Begin autocorrection test
        pitch_change = math.degrees(val[0]) - self.p_tune #round(math.degrees(val[0]), 1)
        self.pitch += pitch_change #* 0.01 

        roll_change = math.degrees(val[1]) #round(math.degrees(val[1]), 1)
        self.roll += roll_change #* 0.01 

        yaw_change = int(val[2] * 100) / 100 # Round value
        self.yaw += yaw_change * 0.01 

        #if self.start:
        #    self.roll_init = roll_change
        #    self.pitch_init = pitch_change
        #self.start = False

        self.error = self.set_point - self.pitch #pitch_change

        self.P_correction = self.P * self.error
        #print("P_correction",self.P_correction)

        #self.iterations += 1
#        print("Pitch: {:+7.3f}\tP Change: {:+7.3f}\tRoll: {:+7.3f}\tR Change: {:+7.3f}\tYaw: {:+7.3f}\tY Change: {:+7.3f}\tError: {:+7.3f}".format(self.pitch, pitch_change, self.roll, roll_change, self.yaw, yaw_change, self.error))
        #if (self.iterations % 10000 == 0):
        #    print("val[0]: {},\tpitch_change: {}\tself.pitch: {}\tself.error: {}\titeraitons: {}".format(val[0], pitch_change, self.pitch, self.error, self.iterations))
        print("val[0]: {:+7.3f},\tpitch_change: {:+7.3f}\tself.pitch: {:+7.3f}\tself.error: {:+7.3f}\titeraitons: {}".format(val[0], pitch_change, self.pitch, self.error, self.iterations))
#        print("val[1]: {:+7.3f},\troll_change: {:+7.3f}\tself.roll: {:+7.3f}\tself.error: {:+7.3f}".format(val[1], roll_change, self.roll, self.error))
        #print("val[1]: {:+7.3f},\troll_change: {:+7.3f}\tself.roll: {:+7.3f}\tself.error: {:+7.3f}".format(val[1], roll_change, self.roll, self.error))


        #a_speed = += self.p * self.

        if (self.P_correction < 0.0):
            rc.set_rotors(a=0.1, b=0.0, c=0.0, d=0.1)
        if (self.P_correction > 0.0):
            rc.set_rotors(a=0.0, b=0.1, c=0.1, d=0.0)
        



pid = PID()

while(True):
    pid.update(sensors.get_data2(), axis=0) # Get data as a list, pass to PID update
#    sensors.get_data()


    
