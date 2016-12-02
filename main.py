import rotor_control as rc
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

        
        
        self.speed_a = HOVER_SPEED
        self.speed_b = HOVER_SPEED
        self.speed_c = HOVER_SPEED
        self.speed_d = HOVER_SPEED

        self.P = P
        self.I = I
        self.D = D
        self.Derivator = Derivator
        self.Integrator = Integrator
        self.Integrator_max = Integrator_max
        self.Integrator_min = Integrator_min

        self.pitch = 0 # Axis 0
        self.roll = 0 # Axis 1
        self.yaw = 0 # Axis 2

        self.set_point = 0.0 # Ideal state for now is hover
        self.error=0.0
        self.P_correction = 0.0

    def update(self, val, axis=0):

        # Begin autocorrection test
        pitch_change = int(val[0] * 100) / 100 # Round value
        self.pitch += pitch_change * 0.01 

        roll_change = int(val[1] * 100) / 100 # Round value
        self.roll += roll_change * 0.01 

        yaw_change = int(val[2] * 100) / 100 # Round value
        self.yaw += yaw_change * 0.01 

        self.error = self.set_point - pitch_change

        print("Pitch",self.pitch,"p change",pitch_change,
              "roll",self.roll,"r change",roll_change,"yaw",self.yaw,"y change",yaw_change,
              "error",self.error)

        self.P_correction = self.P * self.error
        print("P_correction",self.P_correction)

        #a_speed = += self.p * self.

        if (self.P_correction < 0.0):
            rc.set_rotors(a=0.1, b=0.0, c=0.0, d=0.1)
        if (self.P_correction > 0.0):
            rc.set_rotors(a=0.0, b=0.1, c=0.1, d=0.0)
        



pid = PID()

while(True):
    pid.update(sensors.get_data2(), axis=0) # Get data as a list, pass to PID update
#    sensors.get_data()


    
