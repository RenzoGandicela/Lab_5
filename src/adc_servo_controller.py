from hal import hal_servo as servo
from hal import hal_adc as adc
from threading import Thread
import time

def main():
    # Initialise
    adc.init()
    servo.init()

    # Python Threads
    adc_thread = Thread(target=adc.get_adc_value)
    adc_thread.start()
    servo_thread = Thread(target=set_servo_position)

if __name__ == "__main__":
    main()