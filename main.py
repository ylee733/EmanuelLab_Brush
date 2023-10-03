from machine import Pin,UART
import time

# initialize UART communication (pins and bandrate)
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=None, stop=2)
# initialize LED
led = Pin("LED", Pin.OUT)

while True:
    uart.write('t') # sends 't' to arduino
    if uart.any():  # if there is any info from arduino
        # read the info
        data = uart.read()
        # if raspberry recieves 'm' from arduino
        if data== b'm':
        # the led is on
            led.toggle()
        # wait 5 seconds before next iteration
    time.sleep(5) 

