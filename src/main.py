from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_led as LED
import led_control as led
import time

#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    password.append(key)

    if key == 1:
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1, 0)
        lcd.lcd_display_string("Blink LED", 2, 0)
        led.led_control_init()

    if key == 0:
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1, 0)
        lcd.lcd_display_string("OFF LED", 2, 0)
        led.stop_led_thread()
        led.led.set_output(20, 0)

    print(password)


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Initialize LED
    LED.init()

    # Display something on LCD
    lcd.lcd_display_string("Lab 5", 1, 0)
    time.sleep(2)
    lcd.lcd_display_string("LED Control", 1, 0)
    lcd.lcd_display_string("0:Off 1:Blink", 2, 0)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()


# Main entry point
if __name__ == "__main__":
    main()
