import time
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import threading

class SG90_92R_Class:
    def __init__(self, Channel, ZeroOffset):
        self.mChannel = Channel
        self.m_ZeroOffset = ZeroOffset
        self.mPwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.mPwm.set_pwm_freq(60)

    def SetPos(self, pos):
        pulse = (650 - 150) * pos / 180 + 150 + self.m_ZeroOffset
        self.mPwm.set_pwm(self.mChannel, 0, int(pulse))

    def Cleanup(self):
        self.SetPos(90)
        time.sleep(1)

def servo_thread(servo, angles):
    try:
        while True:
            for angle in angles:
                servo.SetPos(angle)
                time.sleep(5)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    Servo1 = SG90_92R_Class(Channel=0, ZeroOffset=-10)
    Servo2 = SG90_92R_Class(Channel=1, ZeroOffset=-10)
    Servo3 = SG90_92R_Class(Channel=2, ZeroOffset=-10)
    Servo4 = SG90_92R_Class(Channel=3, ZeroOffset=-10)
    Servo5 = SG90_92R_Class(Channel=4, ZeroOffset=-10)
    Servo6 = SG90_92R_Class(Channel=6, ZeroOffset=-10)
    Servo7 = SG90_92R_Class(Channel=7, ZeroOffset=-10)
    Servo8 = SG90_92R_Class(Channel=8, ZeroOffset=-10)
    Servo9 = SG90_92R_Class(Channel=9, ZeroOffset=-10)
    Servo10 = SG90_92R_Class(Channel=10, ZeroOffset=-10)
    Servo11 = SG90_92R_Class(Channel=11, ZeroOffset=-10)

    thread1 = threading.Thread(target=servo_thread, args=(Servo1, [0,90]))
    thread2 = threading.Thread(target=servo_thread, args=(Servo2, [0,90]))
    thread3 = threading.Thread(target=servo_thread, args=(Servo3, [0,90]))
    thread4 = threading.Thread(target=servo_thread, args=(Servo4, [0,90]))
    thread5 = threading.Thread(target=servo_thread, args=(Servo5, [0,90]))
    thread6 = threading.Thread(target=servo_thread, args=(Servo6, [0,90]))
    thread7 = threading.Thread(target=servo_thread, args=(Servo7, [0,90]))
    thread8 = threading.Thread(target=servo_thread, args=(Servo8, [0,90]))
    thread9 = threading.Thread(target=servo_thread, args=(Servo9, [0,90]))
    thread10 = threading.Thread(target=servo_thread, args=(Servo10, [0,90]))
    thread11 = threading.Thread(target=servo_thread, args=(Servo11, [0,90]))

    try:
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread7.start()
        thread8.start()
        thread9.start()
        thread10.start()
        thread11.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
        thread9.join()
        thread10.join()
        thread11.join()

    except KeyboardInterrupt:
        pass

    finally:
        Servo1.Cleanup()
        Servo2.Cleanup()
        Servo3.Cleanup()
        Servo4.Cleanup()
        Servo5.Cleanup()
        Servo6.Cleanup()
        Servo7.Cleanup()
        Servo8.Cleanup()
        Servo9.Cleanup()
        Servo10.Cleanup()
        Servo11.Cleanup()
        print("Exit program")
