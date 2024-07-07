# BootPad

BootPad is a simple, customizable 4-button keyboard built using a Raspberry Pi Pico and CircuitPython. It is designed to manage boot menus or other applications that require basic navigation and selection input.

## Features

- **F8 Key**: Button 1 (GP16)
- **Up Arrow Key**: Button 2 (GP17)
- **Down Arrow Key**: Button 3 (GP18)
- **Enter Key**: Button 4 (GP19)

## Components

- Raspberry Pi Pico
- 4 momentary push buttons or keyboard switches (used them)
- Breadboard and jumper wires (optional)

## Circuit GPIOs

Each button should be connected to the corresponding GPIO pin on the Raspberry Pi Pico and ground.

GP16 &rarr; Button 1   
GP17 &rarr; Button 2    
GP18 &rarr; Button 3   
GP19 &rarr; Button 4   


## Installation

1. **Install CircuitPython on Raspberry Pi Pico:**
    1. Download the latest CircuitPython .uf2 file for the Raspberry Pi Pico from the [CircuitPython downloads page](https://circuitpython.org/board/raspberry_pi_pico/).
    2. Connect the Raspberry Pi Pico to your computer while holding down the BOOTSEL button to put it in bootloader mode.
    3. Drag and drop the downloaded .uf2 file onto the Raspberry Pi Pico's drive.

2. **Install the CircuitPython Libraries:**
    - Download the `adafruit-circuitpython-bundle` library bundle from the [CircuitPython Libraries](https://circuitpython.org/libraries) page.
    - Unzip the file and copy the required libraries (usually `adafruit_hid` and `adafruit_debouncer`) to the `lib` folder on the Raspberry Pi Pico.

3. **Upload the Code:**
Save the code as code.py on the Raspberry Pi Pico using [Thonny](https://thonny.org/). The Pico will automatically run the script on startup.

## Usage
Connect the Raspberry Pi Pico to your computer. When you press a button, the corresponding key press (F8, Up, Down, Enter) will be sent to your computer, allowing you to navigate and select options in a boot menu (similar other applications).

## Logging
The script includes logging to the serial console, which can be viewed in Thonny:

Go to View -> Files to see the file browser.  
Click the Stop/Restart Backend button (a red square or green triangle).  
Go to View -> Run to open the serial console.  
Connect to your Raspberry Pi Pico (it should show up as a serial device).  
You will see logs indicating when a button is pressed and which key is sent.  

## License

This project is licensed under the MIT License.

## Acknowledgments  
[CircuitPython](https://circuitpython.org/)  
[Adafruit CircuitPython HID Library ](https://docs.circuitpython.org/projects/hid/en/latest/)   
[Adafruit CircuitPython Debouncer Library ](https://docs.circuitpython.org/projects/debouncer/en/latest/) 
