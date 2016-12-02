imu = 0;
import spidev
import navio.mpu9250


def init():
    global imu
    imu = navio.mpu9250.MPU9250()
    if(imu.testConnection()):
        print("IMU is all good!")
    else:
        print("=========== IMU FAILED TO LOAD ===========")
    imu.initialize()

def get_data():
    if(imu == 0):
        print("CANNOT USE IMU IF NOT INITIALIZED. Make sure to run sensors.init() first")
        return
    m9a, m9g, m9m = imu.getMotion9()

    print "Acc:", "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2]),
    print " Gyr:", "{:+8.3f}".format(m9g[0]), "{:+8.3f}".format(m9g[1]), "{:+8.3f}".format(m9g[2]),
    print " Mag:", "{:+7.3f}".format(m9m[0]), "{:+7.3f}".format(m9m[1]), "{:+7.3f}".format(m9m[2])
