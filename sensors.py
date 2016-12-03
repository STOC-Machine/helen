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

def ensure_imu_loaded():
    if(imu == 0):
        raise ValueError("CANNOT USE IMU IF NOT INITIALIZED. Make sure to run sensors.init() first")

def get_data4():
    ensure_imu_loaded()
    m9a, m9g, m9m = imu.getMotion9()
    return m9g
#    print "Gyroscope:     ", imu.gyroscope_data[2] #Pitch=0, Roll=1, Yaw=2

def get_data3():
    ensure_imu_loaded()
    imu.read_acc()
    return imu.accelerometer_data
#    print "Accelerometer:     ", imu.accelerometer_data[2] #Pitch=0, Roll=1, Yaw=2

def get_data2():
    ensure_imu_loaded()
    imu.read_gyro()
    return imu.gyroscope_data
#    print "Gyroscope:     ", imu.gyroscope_data[2] #Pitch=0, Roll=1, Yaw=2

def get_data():
    ensure_imu_loaded()
    m9a, m9g, m9m = imu.getMotion9()

    print "Acc:", "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2]),
    print " Gyr:", "{:+8.3f}".format(m9g[0]), "{:+8.3f}".format(m9g[1]), "{:+8.3f}".format(m9g[2]),
    print " Mag:", "{:+7.3f}".format(m9m[0]), "{:+7.3f}".format(m9m[1]), "{:+7.3f}".format(m9m[2])
