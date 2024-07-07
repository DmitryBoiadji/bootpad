import board
import digitalio
from adafruit_debouncer import Debouncer
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Setup the pins for each button
button_pins = {
    "F8": board.GP16,
    "UP": board.GP17,
    "DOWN": board.GP18,
    "ENTER": board.GP19
}

# Corresponding keycodes
keycodes = {
    "F8": Keycode.F8,
    "UP": Keycode.UP_ARROW,
    "DOWN": Keycode.DOWN_ARROW,
    "ENTER": Keycode.ENTER
}

# Initialize buttons
buttons = {}
for key, pin in button_pins.items():
    button_pin = digitalio.DigitalInOut(pin)
    button_pin.direction = digitalio.Direction.INPUT
    button_pin.pull = digitalio.Pull.UP
    buttons[key] = Debouncer(button_pin)

# Setup the keyboard
keyboard = Keyboard(usb_hid.devices)

print("Starting the button press to key press script")

while True:
    for key, button in buttons.items():
        button.update()
        if button.fell:
            print(f"{key} button pressed")
            keyboard.send(keycodes[key])
            print(f"{keycodes[key]} key sent")
